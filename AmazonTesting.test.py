import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By

# Page classes
from AmazonHomePage import AmazonHomePage
from ProductPage import AmazonProductPage

def test_amazon_purchase():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://www.amazon.in/")

    # Interact with home page
    home_page = AmazonHomePage(driver)
    home_page.search_product("iPhone 13")

    # Get product list and open a product
    product_list = home_page.get_product_list()
    print([product.text for product in product_list])

    # Open the 4th product if it exists
    home_page.open_product(3)

    # Switch to the new window after clicking the product
    open_window = driver.window_handles
    driver.switch_to.window(open_window[1])

    # Interact with product page
    product_page = AmazonProductPage(driver)
    product_page.click_buy_now()

    # Fill in login details
    product_page.enter_email("abc@gmail.com")
    product_page.click_continue()
    product_page.enter_password("125654")
    product_page.click_sign_in()

    print("Test completed successfully.")
    time.sleep(random.uniform(2, 5))
    driver.quit()

if __name__ == "__main__":
    test_amazon_purchase()
