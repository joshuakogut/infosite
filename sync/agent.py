import json
import logging

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.remote_connection import LOGGER
from urllib3.connectionpool import log as urllibLogger

LOGGER.setLevel(logging.WARNING)
urllibLogger.setLevel(logging.WARNING)


class Agent(webdriver.Remote):
    def __init__(
        self, browser="chrome", headless=False, remote_url=None, cookie="generic"
    ):
        """
        Initializes the Agent with specified browser, headless mode, and remote URL.
        """
        self.cookies_namespace = cookie

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.WARNING)

        options = self._get_browser_options(browser, headless)
        capabilities = options.to_capabilities()

        if remote_url:
            self.remote_url = remote_url
        else:
            # self.remote_url = "http://192.168.1.135:4444/wd/hub"
            self.remote_url = "http://localhost:4444/wd/hub"

        super().__init__(self.remote_url, options=options)

    def _get_browser_options(self, browser, headless):
        """
        Returns browser-specific options with common configurations.
        """
        if browser == "chrome":
            options = Options()
            if headless:
                options.add_argument("--headless")
            options.add_argument("--disable-infobars")
            options.add_argument("--window-size=1800,1600")
            options.add_argument(
                "--user-agent=Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36"
            )
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-extensions")
            prefs = {}
            prefs["profile.default_content_settings.popups"] = 0
            prefs["download.default_directory"] = (
                "/mnt/share/"  # z: maps to \\localhost\share
            )
            options.add_experimental_option("prefs", prefs)
            return options
        else:
            raise ValueError(f"Unsupported browser: {browser}")

    def wait_for_ajax(self):
        """
        Waits for AJAX requests to complete and the document to be ready.
        """
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
            self.logger.error("Error waiting for AJAX:", exc_info=True)

    def load_cookies(self):
        """
        Loads cookies from a file and adds them to the browser session.
        """
        cookie_file = "cookies/%s.json" % self.cookies_namespace
        self.logger.info("Loading cookies from: %s", cookie_file)
        try:
            with open(cookie_file, "r") as handle:
                cookies = json.load(handle)
                for cookie in cookies:
                    if "expiry" in cookie:
                        cookie["expires"] = cookie["expiry"]
                        del cookie["expiry"]
                    del cookie["httpOnly"]
                    del cookie["sameSite"]
                    self.add_cookie(cookie)
        except FileNotFoundError:
            self.logger.warning("Cookie file not found: %s", cookie_file)
        except Exception as e:
            self.logger.error("Error loading cookies:", exc_info=True)

    def store_cookies(self):
        """
        Saves the current browser cookies to a file.
        """
        cookie_file = "cookies/%s.json" % self.cookies_namespace
        self.logger.info("Saving cookies to: %s", cookie_file)
        with open(cookie_file, "w") as handle:
            json.dump(self.get_cookies(), handle)

    def get(self, uri):
        """
        Logs the URL before navigating using the GET request.
        """
        self.logger.debug("Explicit GET request: %s", uri)
        return super().get(uri)
