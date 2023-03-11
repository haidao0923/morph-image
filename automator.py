from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
import requests


driver = webdriver.Chrome('C:/Users/haixd/AppData/Local/Programs/Python/Python36-32/Scripts/chromedriver')
url = 'https://en.pixiz.com/template/Fusion-of-two-faces-1630'
driver.get(url)
image1 = "C:/Users/haixd/Desktop/AutomateFaceMorph/jacob_abernethy_0.png"
image2 = "C:/Users/haixd/Desktop/AutomateFaceMorph/joy_arulraj_0.png"
driver.find_element(By.ID, "upload-file-1").send_keys(image1)
driver.find_element(By.ID, "upload-file-2").send_keys(image2)
driver.find_element(By.ID, "upload-submit-button").click()
button_container = driver.find_element(By.CLASS_NAME, "nologo")
link = driver.find_element(By.XPATH, '//*[@id="p-result"]/div/div[3]/div/div[3]/ul/li[5]/a').get_attribute('href')
print("Test", link)
morphed_image = requests.get(link).content
with open("morphed_image.png", 'wb') as handler:
    handler.write(morphed_image)

time.sleep(5)
input()