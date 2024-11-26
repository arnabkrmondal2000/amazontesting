from selenium.webdriver.common.by import By

class AmazonProductPage:
    def __init__(self, driver):
        self.driver = driver

    def click_buy_now(self):
        buy_now_button = self.driver.find_element(By.CSS_SELECTOR, "span[id='submit.buy-now']")
        buy_now_button.click()

    def enter_email(self, email):
        email_field = self.driver.find_element(By.CSS_SELECTOR, "#ap_email")
        email_field.send_keys(email)

    def click_continue(self):
        continue_button = self.driver.find_element(By.CSS_SELECTOR, ".a-button-input")
        continue_button.click()

    def enter_password(self, password):
        password_field = self.driver.find_element(By.CSS_SELECTOR, "#ap_password")
        password_field.send_keys(password)

    def click_sign_in(self):
        sign_in_button = self.driver.find_element(By.CSS_SELECTOR, "#signInSubmit")
        sign_in_button.click()
