import json

import logging
from selenium.webdriver.remote.remote_connection import LOGGER

LOGGER.setLevel(logging.WARNING)

from urllib3.connectionpool import log as urllibLogger

urllibLogger.setLevel(logging.WARNING)

from portal import Logger

logger = Logger("sync.agent")

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# from selenium_recaptcha_solver import RecaptchaSolver
from selenium.webdriver.support import expected_conditions as EC

# import selenium.webdriver.common.devtools.v111 as devtools
from selenium.webdriver.support.ui import WebDriverWait


class Agent(webdriver.Remote):

    def __init__(self, headless=False):

        options = Options()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--disable-infobars")
        options.add_argument("--window-size=1800,1600")
        options.add_argument(
            "--user-agent=Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36"
        )
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-extensions")
        prefs = {}
        prefs["profile.default_content_settings.popups"] = 0
        prefs["download.default_directory"] = "s:\\joshk\\downloads"
        options.add_experimental_option("prefs", prefs)

        capabilities = options.to_capabilities()
        return super().__init__("http://192.168.1.135:4444/wd/hub", options=options)

    def wait_for_ajax(self):
        wait = WebDriverWait(self, 15)
        try:
            wait.until(
                lambda driver: driver.execute_script("return jQuery.active") == 0
            )
            wait.until(
                lambda driver: driver.execute_script("return document.readyState")
                == "complete"
            )
        except Exception as e:
            pass

    def load_cookies(self):
        logger.info("loading cookies")
        try:

            with open("cookies.json", "r") as handle:
                cookies = json.load(handle)
                for c in cookies:
                    if "expiry" in c:
                        c["expires"] = c["expiry"]
                        del c["expiry"]
                        del c["httpOnly"]
                        del c["sameSite"]
                    self.add_cookie(c)
        except Exception as ex:
            logger.error("threw cookie exception")

    def store_cookies(self):
        logger.info("saving cookies")
        with open("cookies.json", "w") as handle:
            json.dump(self.get_cookies(), handle)

    def get(self, uri):
        logger.debug("explicit GET request", URL=uri)
        return super().get(uri)
