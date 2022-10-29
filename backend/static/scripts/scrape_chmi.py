import os
import time
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


def chmiscrape():

    # Open web
    print("Starting up ...")
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )

    print("Scraping content ...")
    driver.get(
        "https://www.chmi.cz/predpovedi/predpovedi-pocasi/ceska-republika/tydenni-predpoved"
    )

    sleep(1)

    ##Parse html
    print("Saving data ...")
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    with open(
        "/home/evzen/doc/script/python/fastapi/vedro/backend/static/files/chmi.html",
        "w",
        encoding="utf-8",
    ) as file:
        file.write(str(soup))

    print("Quiting ...")
    sleep(1)

    driver.quit()
