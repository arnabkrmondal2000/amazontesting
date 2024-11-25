import time

from selenium import webdriver
## in selenium pakage their is a class called webDriver

##chrome driver service Selenium

# driver = webdriver.Chrome()
# driver.get("https://rahulshettyacademy.com")
## this method is applicable for latest chrome version or maximum others

## if it is old chrome version or had some vpn connection

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com")
driver.maximize_window() ##for maximize window
print(driver.title)
print(driver.current_url)









time.sleep(2) ##time is class in python libery which delay the execution