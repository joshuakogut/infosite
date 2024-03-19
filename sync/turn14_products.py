#!/usr/bin/env python3

import os, sys, time, glob, csv
import django
import zipfile
import shutil

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portal.settings")
django.setup()


from portal import Logger

logger = Logger("sync.host.turn14")

from portal.models import *
import pandas as pd
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from sync.agent import *
from sync.host.volusion import update_stock, VolusionError

download_dir = "/mnt/share/"
pref_url = "https://turn14.com/export_preferences.php"
feed_url = "https://turn14.com/export.php?action=inventory_feed"
t14_user = "lcengineering"
t14_pass = "***REMOVED***!"

if __name__ == "__main__":

    driver = Agent()
    try:

        logger.info("logging into turn14")
        driver.get(pref_url)

        uname = driver.find_element("xpath", '//input[@name="username"]')
        passw = driver.find_element("xpath", '//input[@name="password"]')
        submit = driver.find_element("xpath", '//button[@type="submit"]')

        uname.send_keys(t14_user)
        passw.send_keys(t14_pass)
        submit.click()

        waitfor = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//a[text()="LOGOUT"]'))
        )
        logger.info(login="Completed")
        driver.store_cookies()

        # clear old zips
        oldzips = glob.glob(download_dir + "*.zip")
        oldcsvs = glob.glob(download_dir + "*.csv")
        for file in oldzips + oldcsvs:
            os.remove(file)

        driver.get(feed_url)
        time.sleep(5)
        logger.info("done getting feed, thanks")
        driver.quit()

        feed_data = None
        for file in glob.glob(download_dir + "*.zip"):
            logger.info("found feed result", path=file)

            archive = zipfile.ZipFile(file, "r")
            names = archive.namelist()
            for compressed in names:
                if compressed.endswith(".csv"):
                    archive.extract(compressed, download_dir)
                    shutil.move(download_dir + compressed, download_dir + "turn14.csv")
                    logger.info(
                        "extracted",
                        archive=file,
                        file=compressed,
                        dest=download_dir + "turn14.csv",
                    )
                    break
            break

        """with open('/tmp/turn14.csv') as handle:
            reader = csv.reader(handle, delimiter=',', quotechar='"')
            next(reader)"""

        t14_prods = Tbproductsupplier.objects.filter(
            vendor__name="Turn 14 Distribution"
        ).exclude(product__productid__iendswith="-old")
        active_skus = set(
            [d["vendorproductid"] for d in t14_prods.values("vendorproductid")]
        )

        df = pd.read_csv(download_dir + "turn14.csv")
        for index, row in df.iterrows():
            try:
                if (
                    row["InternalPartNumber"] in active_skus
                    or row["PartNumber"] in active_skus
                ):
                    ps = t14_prods.get(
                        Q(vendorproductid=row["InternalPartNumber"])
                        | Q(vendorproductid=row["PartNumber"])
                    )
                    ps.set_remote_stock(int(row["Stock"]))
                    ps.save()

                    update_stock(
                        [
                            (
                                ps.product.productid,
                                ps.remotestock,
                                "Turn 14",
                                ps.vendorproductid,
                            )
                        ]
                    )

            except ObjectDoesNotExist:
                logger.warning(
                    "does not exist",
                    vendorproductid=row[0],
                    other=row[1],
                )
            except MultipleObjectsReturned:
                logger.warning(
                    "fucked up, multiple supplier results",
                    vendorproductid=row[0],
                    matches=[
                        ps.product.productid
                        for ps in t14_prods.filter(
                            Q(vendorproductid=row["InternalPartNumber"])
                            | Q(vendorproductid=row["PartNumber"])
                        )
                    ],
                )

            except:
                logger.exception("issue with something in the productsupplier search")

    finally:
        try:
            driver.quit()
        except:
            pass
