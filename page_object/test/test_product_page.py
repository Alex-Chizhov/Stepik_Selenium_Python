from page_object.pages.product_page import ProductPage
from page_object.tests_data import promo_links
from page_object.pages.basket_page import BasketPage
from page_object.pages.login_page import LoginPage
from page_object.pages.main_page import MainPage
import pytest

# -m add_to_basket_user для запуска только тестов в этом классе
@pytest.mark.add_to_basket_user
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def prepare_user(self, browser):
        page = LoginPage(browser)
        page.go_to_login_page()
        page.register_new_user()
        main_page = MainPage(browser)
        main_page.should_thanks_for_registering_message()
        yield
        # Удаляем пользователя (В учебном курсе не реализуем)

    @pytest.mark.xfail(reason="Negative test (Should be fail)")
    def test_negative_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-girl-who-played-with-non-fire_203/"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_cart_item()
        page.check_main_message_not_present()

    def test_user_can_add_to_cart(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_cart_item()


@pytest.mark.parametrize('link', promo_links)
def test_add_to_cart_promo(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart_item()
    page.solve_quiz_and_get_code()
    page.check_product_name_with_main_message()
    page.check_price_with_price_message()

def test_positive_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-girl-who-played-with-non-fire_203/"
    page = ProductPage(browser, link)
    page.open()
    page.check_main_message_not_present()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page_by_link()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page_by_button_in_header()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.check_basket_is_empty()
    basket_page.check_there_is_message_basket_is_empty()

@pytest.mark.xfail(reason="Negative test (Should be fail)")
def test_negative_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-girl-who-played-with-non-fire_203/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart_item()
    page.check_main_message_disappeared()