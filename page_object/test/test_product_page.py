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