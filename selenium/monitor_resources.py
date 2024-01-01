# coding: utf-8
import psutil
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

URL = "https://lab-fuwari.com/"


if __name__ == "__main__":
    print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")
    print(f"Memory Usage: {psutil.virtual_memory().percent}%")
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-plugins")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    driver.get(URL)
    selector = "//div/img[@src='/assets/images/thumbnail.png']"
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, selector)))
    driver.close()
