from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math

class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_correct_product_name_in_message(self, expected_name):
        product_in_message = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_NAME).text
        assert expected_name == product_in_message, \
            f"Expected product name '{expected_name}', but got '{product_in_message}'"

    def should_be_correct_product_price_in_message(self, expected_price):
        price_in_message = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_PRICE).text
        assert expected_price == price_in_message, \
            f"Expected product price '{expected_price}', but got '{price_in_message}'"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should be"

    def solve_quiz_and_get_code(self):
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            x = int(alert_text.split("x = ")[-1].split()[0])
            answer = str(math.log(abs(12 * math.sin(x))))
            alert.send_keys(answer)
            alert.accept()
            try:
                alert = self.browser.switch_to.alert
                print(f"Second alert: {alert.text}")
                alert.accept()
            except NoAlertPresentException:
                pass
        except NoAlertPresentException:
            print("No alert presented")
