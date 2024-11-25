

import time
from selenium.webdriver import ActionChains
##from tkinter.tix import Select
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element(By.LINK_TEXT, "Click Here").click()

windowopen = driver.window_handles

driver.switch_to.window(windowopen[1])
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close() ## it is use to close the child window
driver.switch_to.window(windowopen[0])
print(driver.find_element(By.TAG_NAME, "h3").text)
time.sleep(2)