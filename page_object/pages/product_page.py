from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_to_cart_item(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

    def check_product_name_with_main_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        main_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ADDED_TO_CART_MASSAGE).text
        assert product_name == main_message, 'Корректного имени продукта нет в сообщении о добавлении в корзину'

    def check_price_with_price_message(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        price_message = self.browser.find_element(*ProductPageLocators.TOTAL_PRICE_MASSAGE).text
        assert price == price_message, 'Корректной цены нет в сообщение о добавлении товара в корзину'

    def check_main_message_not_present(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_NAME_ADDED_TO_CART_MASSAGE), \
            "Success message is presented, but should not be"

    def check_main_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_NAME_ADDED_TO_CART_MASSAGE), \
            "Success message is not disappeared"