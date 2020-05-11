from page_object.pages.product_page import ProductPage
from page_object.tests_data import promo_links
import pytest


def test_add_to_cart(browser):
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

@pytest.mark.xfail(reason="Negative test (Should be fail)")
def test_negative_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-girl-who-played-with-non-fire_203/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart_item()
    page.check_main_message_not_present()

def test_positive_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-girl-who-played-with-non-fire_203/"
    page = ProductPage(browser, link)
    page.open()
    page.check_main_message_not_present()

@pytest.mark.xfail(reason="Negative test (Should be fail)")
def test_negative_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-girl-who-played-with-non-fire_203/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart_item()
    page.check_main_message_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()