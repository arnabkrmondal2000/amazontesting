## Mouse Hover practice


import time
from selenium.webdriver import ActionChains
##from tkinter.tix import Select
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

action = ActionChains(driver)
# action.click_and_hold()
# action.context_click() ##Right Click
# action.double_click()
# action.drag_and_drop()
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
# action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()
