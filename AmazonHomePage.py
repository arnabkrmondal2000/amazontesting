from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

class AmazonHomePage:
    def __init__(self, driver):
        self.driver = driver

    def search_product(self, product_name):
        search_box = self.driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox")
        search_box.send_keys(product_name)
        search_button = self.driver.find_element(By.CSS_SELECTOR, "#nav-search-submit-button")
        search_button.click()

    def get_product_list(self):
        product_list = self.driver.find_elements(By.CSS_SELECTOR, ".a-size-medium.a-color-base.a-text-normal")
        return product_list

    def open_product(self, index=3):
        product_list = self.get_product_list()
        if len(product_list) >= index:
            product_list[index].click()
        else:
            print("Less than four products found")
