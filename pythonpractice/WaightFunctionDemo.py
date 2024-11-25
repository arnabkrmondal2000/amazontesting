import time
##from tkinter.tix import Select
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")

time.sleep(2)

reslutsList = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(reslutsList)
print(count)
assert  count>0


##chainning of web element on parent (resultsList) to child
for result in reslutsList:
    result.find_element(By.XPATH, "div/button").click()
driver.find_element(By.CSS_SELECTOR, "img[alt = 'Cart']").click()
driver.find_element(By.XPATH, "//button[text() = 'PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
time.sleep(5)
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)
time.sleep(2)


## implecit weight --> it is like a global timout, if any element not shown in the page it weight max that sec for that