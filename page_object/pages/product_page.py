from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_to_cart_item(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()
        self.solve_quiz_and_get_code()
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        main_message = self.browser.find_element(*ProductPageLocators.SUCCESSFULLY_ADDED_TO_CART_MASSAGE).text
        price_message = self.browser.find_element(*ProductPageLocators.TOTAL_PRICE_MASSAGE).text
        assert product_name in main_message, 'Корректного имени продукта нет в сообщении о добавлении в корзину'
        assert price in price_message, 'Корректной цены нет в сообщение о добавлении товара в корзину'