from .locators import BasketPageLocators
from .base_page import BasePage

class BasketPage(BasePage):

    def check_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), "There is an item in basket"

    def check_there_is_message_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.MASSAGE_BASKET_IS_EMPTY), "There is not message: basket is empty"