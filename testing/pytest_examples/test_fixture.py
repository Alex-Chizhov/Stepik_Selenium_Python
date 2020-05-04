import pytest
from selenium import webdriver


# scope = “function”, “class”, “module”, “session”
@pytest.fixture(scope="class")
def browser():
    # код выполнится до выполнения теста
    print("\n_start browser for test_")
    browser = webdriver.Chrome()
    yield browser
    # код выполнится после завершения теста
    print("\n_quit browser_")
    browser.quit()


class TestMainPage1:
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")