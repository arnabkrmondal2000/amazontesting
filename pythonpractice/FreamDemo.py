

import time
from selenium.webdriver import ActionChains
##from tkinter.tix import Select
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By




driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/iframe")

iframe = driver.find_element(By.ID, "mce_0_ifr")  # Adjust the ID based on your iframe
driver.switch_to.frame(iframe)

driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("I am able to clear it")
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID,"tinymce").clear()
driver.find_element(By.ID,"tinymce").send_keys("I am able to automate frames")




