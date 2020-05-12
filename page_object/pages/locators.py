from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group a.btn-default")

class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRICE = (By.CSS_SELECTOR, "div.product_main .price_color")
    PRODUCT_NAME_ADDED_TO_CART_MASSAGE = (By.XPATH, "//div[text()[contains(.,'has been added to your basket')]]/strong")
    TOTAL_PRICE_MASSAGE = (By.XPATH, "//*[text()[contains(.,'Your basket total is now')]]/strong")


class BasketPageLocators:
    BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items")
    MASSAGE_BASKET_IS_EMPTY = (By.XPATH, "//div[@class='content']//p[text()[contains(.,'Your basket is empty')]]")