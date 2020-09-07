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

# search = driver.find_element_by_name("s")
# search.send_keys("test")
# search.send_keys(Keys.RETURN)

# try:
#     main = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "main"))
#     )

#     articles = main.find_element_by_tag_name("article")
#     for article in articles:
#         header = article.find_element_by_class_name("entry_summary")
#         print(header.text)

# finally:
#     driver.quit()

link = driver.find_element_by_link_text("Python Programming")
link.click()

# need to wait til element exists before clicking
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    element.click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sow-button-19310003"))
    )
    element.click()

    # to clear a field before if its a text field
    # element.clear()

    # now back to homepage
    driver.back()
    driver.back()
    driver.back()

    # can use forward too
    # driver.forward()


except Exception:
    driver.quit()

