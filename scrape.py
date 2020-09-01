#  had to install chromedriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

PATH = "/Users/brianarchibald/Desktop/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net")
print(driver.title)  # title of the site

search = driver.find_element_by_name("s")
search.send_keys("test")
search.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
except Exception as e:
    print(e)
    driver.quit()

main = driver.find_element_by_id("main")
print(main.text)
