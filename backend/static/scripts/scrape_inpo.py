import os
import time
import requests
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


# Open web
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
sleep(1)
driver.get("https://www.in-pocasi.cz/")
sleep(1)

##Parse html
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

# Save html to disk
# all_ps = soup.find_all("p")

with open(
    "/home/evzen/doc/script/python/fastapi/vedro/backend/static/files/inp.html",
    "w",
    encoding="utf-8",
) as file:
    file.write(str(soup))

sleep(1)
driver.quit()
