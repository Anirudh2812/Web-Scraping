from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging

#to download webdriver - https://sites.google.com/chromium.org/driver/
#chromedriver ver (140.0.7339.207)

#making a log file for logs
logging.basicConfig(
    filename="Web_Scraping.log", level=logging.INFO, 
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logging.info("the app has started")

try:
    service = Service(executable_path = "./chromedriver")
    driver = webdriver.Chrome(service = service)
except Exception as e:
    logging.error(f"ChromeDriver failed: {e}")

selem = input("please enter which product you want to search: ")

#Enter the website to visit
driver.get("https://www.amazon.in/")

#click on continue shopping button 
try:
    button = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "a-no-js"))
    )
    logging.info("Button appeared, clicking...")
    button.click()
except Exception as e:
    logging.info(e)
    logging.info("Button never showed up, continuing...")

#wait for the HTML element to be on the page before parsing
WebDriverWait(driver, 2).until(
    EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
)

# entering the query in searchbox
input_element1 = driver.find_element(By.ID, "twotabsearchtextbox")
input_element1.click()
input_element1.clear()
input_element1.send_keys(f"{selem}"+Keys.ENTER)



# time.sleep(30)

# driver.quit()