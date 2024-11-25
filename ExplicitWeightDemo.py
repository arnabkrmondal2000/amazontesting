import time

from selenium.webdriver.support import wait, expected_conditions
##from tkinter.tix import Select
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(2)
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

### Sum validation

prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")

sum = 0
for price in prices:
    sum = sum + int(price.text)


print(sum)
totalamount = driver.find_element(By.CSS_SELECTOR, ".totAmt").text
assert sum == int(totalamount)


driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
# time.sleep(5)

## amout and discount validation
amount = driver.find_element(By.CSS_SELECTOR, ".totAmt").text
discount = driver.find_element(By.CSS_SELECTOR, ".discountAmt").text
print(amount)
print(discount)

assert int(amount) == int(discount)

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)
time.sleep(2)


## implecit weight --> it is like a global timout, if any element not shown in the page it weight max that sec for that
## explicit weight --> it target specific element