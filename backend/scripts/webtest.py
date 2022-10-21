import os
import time
import shutil
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# Open web
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver = webdriver.Chrome("/home/evzen/doc/data/chromedriver")
driver.maximize_window()
# driver.execute_script("document.body.style.zoom = 'zoom 80%'")
driver.get(
    "https://www.chmi.cz/predpovedi/predpovedi-pocasi/ceska-republika/tydenni-predpoved"
)
sleep(2)
##Agree to conditions
sat = driver.find_element(By.XPATH, "//*[@class='textik1']")

print(sat.text)
# user_name.send_keys("evzen")
# sleep(5)
# agree.click()


# #Deselect Approved
# deselect_approved = driver.find_element(By.XPATH, '//input[@aria-label="Approved"]/following::div')
# deselect_approved.click()
# sleep(0.05)
#

sleep(5)
driver.quit()
