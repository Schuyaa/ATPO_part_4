from .base_page import BasePage
from selenium.webdriver.common.by import By

class BasketPage(BasePage):
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*self.BASKET_ITEMS), \
            "Basket contains items, but it should be empty"

    def should_be_empty_basket_text(self):
        assert self.is_element_present(*self.EMPTY_BASKET_TEXT), \
            "Empty basket text is not presented"
        text = self.browser.find_element(*self.EMPTY_BASKET_TEXT).text
        assert "Your basket is empty" in text, \
            "Empty basket message is incorrect or missing"
