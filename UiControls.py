import time
##from tkinter.tix import Select
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

for chek in checkboxes:
    if chek.get_attribute("value") == "option2":
        chek.click()
        assert chek.is_selected()
        break

radioButtons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radioButtons[2].click()
assert radioButtons[2].is_selected()


time.sleep(2)