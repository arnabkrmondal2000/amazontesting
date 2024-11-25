import time
import random
##from tkinter.tix import Select
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.amazon.in/")

driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox").send_keys("iPhone 13")
driver.find_element(By.CSS_SELECTOR, "#nav-search-submit-button").click()
productList = driver.find_elements(By.CSS_SELECTOR, ".a-size-medium.a-color-base.a-text-normal")

list = []
for product in productList:
    list.append(product.text)
print(list)

if len(productList)>=4:
    productList[3].click()
else:
    print("less than four products found")

openWindow = driver.window_handles
driver.switch_to.window(openWindow[1])
driver.find_element(By.CSS_SELECTOR, "span[id='submit.buy-now']").click()
driver.find_element(By.CSS_SELECTOR, "#ap_email").send_keys("abc@gmail.com")
driver.find_element(By.CSS_SELECTOR, ".a-button-input").click()
driver.find_element(By.CSS_SELECTOR, "#ap_password").send_keys("125654")
driver.find_element(By.CSS_SELECTOR, "#signInSubmit").click()
#####
Error_Message = driver.find_element(By.CSS_SELECTOR, "ul[class='a-unordered-list a-nostyle a-vertical a-spacing-none'] li").text
print(Error_Message)
time.sleep(random.uniform(2, 5))


print("All correct")
#print(len(productList))
time.sleep(2)