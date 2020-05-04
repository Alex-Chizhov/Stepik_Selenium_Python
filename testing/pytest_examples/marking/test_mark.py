"""
https://docs.pytest.org/en/latest/skipping.html

ключ -rA используется для вывода всех дополнительных сообщений отчета в консоли

Чтобы запустить тест с нужной маркировкой,
нужно передать в командной строке параметр -m и нужную метку:
    pytest -m smoke test_mark.py

Так же можно маркировать целый тестовый класс.
В этом случае маркировка будет применена ко всем тестовым методам, входящим в класс.

Для запуска всех тестов, не отмеченных как smoke, нужно выполнить команду:
    pytest -m "not smoke" test_mark.py

Для запуска тестов с разными метками:
     pytest -m "smoke or regression" test_mark.py

Для запуска тестов с двумя метками:
     pytest -m "smoke and regression" test_mark.py

Для пропуска теста, его отмечают в коде маркой:
    @pytest.mark.skip

Для пометки падающего теста, его отмечают в коде маркой:
    @pytest.mark.xfail(reason="Причина - баг фиксят")
Чтобы увидеть сообщение в консоли c причиной,
при запуске нужно добавлять параметр pytest -rx.

Если тетсы помеченные @pytest.mark.xfail и баг починен тетс стал проходить
он помечается категорией XPASS.
Чтобы получить подробную информацию по XPASS-тестам в отчете консоли
s для skipped tests:
    pytest -rxXs test_mark.py
"""

import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1:

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_guest_should_see_button_find(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("input.btn")

    @pytest.mark.skip
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_guest_should_see_button_dropdown(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("button[data-toggle='dropdown']")

    @pytest.mark.xfail(reason="fixing this bug right now")
    def test_guest_should_see_search_button_on_the_main_page1(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("input.btn.btn-default1")

    @pytest.mark.xfail(reason="fixing this bug right now")
    def test_guest_should_see_search_button_on_the_main_page2(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("input.btn.btn-default")