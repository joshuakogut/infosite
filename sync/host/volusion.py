import requests
import xmltodict
import re
from bs4 import BeautifulSoup
from xml.sax.saxutils import escape
from portal.settings import VOL_USER, VOL_PASS


class VolusionError(Exception):
    pass


product_get = "http://www.lceperformance.com/net/WebService.aspx?Login=%s&EncryptedPassword=%s&EDI_Name=Generic\\Products&SELECT_Columns=p.LastModBy,p.LastModified,p.ProductCode,p.ProductName,pd.ProductDescription,pe.ProductPrice,pm.ExtInfo,pm.ProductFeatures,pm.TechSpecs"


product_update = "https://www.lceperformance.com/net/WebService.aspx?Login=%s&EncryptedPassword=%s&Import=Update"


def get_products(limit=99):
    infos = []
    NextPage = True
    while NextPage:
        response = requests.get(product_get % (VOL_USER, VOL_PASS))
        soup = BeautifulSoup(response.text, features="xml")
        data = soup.find_all("Products")

        if len(data) == 0:
            break

        for product in data:
            info = {}
            for child in product.children:
                if child is not None and child.name is not None:
                    info[child.name] = child.text
            infos.append(info)

        if len(infos) > limit:
            NextPage = False

    return infos


def update_products(products):  # list[dict[string:any]]
    headers = {"Content-Type": "application/xml; charset=utf-8"}

    xml = '<?xml version="1.0" encoding="utf-8" ?><xmldata>'
    for product in products:
        xml += "<Products>"

        escapables = ["ProductDescription"]
        for key in product.keys():
            content = product[key]
            if key in escapables:
                content = escape(product[key])
            xml += "	<%s>%s</%s>" % (key, content, key)

        xml += "</Products>"

    xml += "</xmldata>"

    r = requests.post(
        product_update % (VOL_USER, VOL_PASS), data=xml.encode("utf-8"), headers=headers
    )

    if r.status_code != 200:
        raise VolusionError("Server didn't return a 200")

    return r
