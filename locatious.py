import time
##from tkinter.tix import Select
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")

## locaters in selenium : ID, Xpath, CSSSelector, Name, linkText
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Arnab Kr Mondal")
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()

## if we want to create Xpath of any element we jus write
##  //tagname[@attribute = 'value'] --> // input[@type = 'submit'], '#id' shotcut to find cssselector


## handle static dropdown using selenium
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_index(0)
dropdown.select_by_visible_text("Female")
# dropdown.select_by_value() ##if value is define


driver.find_element(By.XPATH, "//input[@type = 'submit']").click()

message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message

## CSS selector as locaters
## tagname[attribute = 'value']




time.sleep(2)