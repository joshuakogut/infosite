#!/usr/bin/env python3

import time
import os
import sys
import re

from portal import Logger
from portal.settings import TG_USER, TG_PASS

logger = Logger("sync.host.trailgear")

from sync.agent import *


root_url = "https://trail-gear.com"
search_url = "https://trail-gear.com/catalogsearch/result/?q=%s"
history_url = "https://trail-gear.com/sales/order/history/"


class ScrapedProduct:
    def __init__(self, sku, name, price, stock=0):
        self.sku = sku
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return "<ScrapedProduct %s>" % (self.sku)


class ScrapedOrder:
    def __init__(self, status, ponumber, packages):
        self.status = status
        self.ponumber = ponumber
        self.packages = packages

    def __str__(self):
        return "<ScrapedOrder %s>" % (self.ponumber)


def search_sku(driver, sku):
    logger.debug(search_sku=sku)

    driver.get(search_url % sku)
    sel = driver.find_elements("xpath", '//a[@class="product-item-link"]')
    uris = [el.get_attribute("href") for el in sel]
    for uri in uris:
        driver.get(uri)
        esku = driver.find_element("xpath", '//div[@itemprop="sku"]')
        if esku.text.lower() == sku.lower():
            name = (driver.find_element("xpath", '//h1[@class="page-title"]').text,)
            price = driver.find_element(
                "xpath", '//span[@data-price-type="finalPrice"]'
            ).text

            stock = "0 IN STOCK"
            search = driver.find_elements(
                "xpath",
                '//div[@class="amstockstatus-status-container stock available"]',
            )
            if len(search) > 0:
                stock = search[0].text
            try:
                match = re.findall(r"([0-9]+)", stock)
                if len(match) > 0:
                    stock = int(match[0])
                else:
                    stock = 0
            except IndexError:
                logger.error("fix this, probably 'limited stock' on %s" % esku)
                stock = 0

            return ScrapedProduct(esku.text, name, price, stock)
    return None


def check_login(driver):
    loggedin = driver.find_elements("xpath", '//*[@class="logged-in"]')
    if len(loggedin) > 0:
        return True

    try:
        # Clear cookie popup
        els = driver.find_elements(
            "xpath", '//*[@class="btn-cookie btn-cookie-accept"]'
        )
        [e.click() for e in els]
    except Exception:
        pass

    uname = driver.find_elements("name", "login[username]")
    passw = driver.find_elements("name", "login[password]")
    btn = driver.find_elements("id", "send2")

    if len(uname) == 0:
        return True

    uname[0].send_keys(TG_USER)
    passw[0].send_keys(TG_PASS)
    btn[0].click()
    waitfor = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@class="logged-in"]'))
    )
    logger.info(login="Completed")
    driver.store_cookies()
    return True


def search_order(driver, ponumber):
    driver.get(history_url)
    waitfor = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "my-orders-table_wrapper"))
    )

    driver.find_element("xpath", '//input[@type="search"]').send_keys(str(ponumber))
    driver.wait_for_ajax()

    status = "404"
    statuses = driver.find_elements(
        "xpath", '//table[@id="my-orders-table"]/tbody/tr[@role="row"]/td[6]'
    )
    if len(statuses) > 0:
        status = statuses[0].text

    btn = driver.find_elements("xpath", '//a[@class="action view"]')
    trackings = []
    if len(btn) > 0:
        driver.find_elements("xpath", '//span[@class="order-status"]')
        href = btn[0].get_attribute("href")
        driver.get(href.replace("view", "shipment"))

        trackings += [
            el.text
            for el in driver.find_elements(
                "xpath", '//dd[@class="tracking-content"]/a/span'
            )
        ]

    return ScrapedOrder(status, ponumber, trackings)
