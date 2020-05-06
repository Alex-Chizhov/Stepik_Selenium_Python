"""
модуль pytest-rerunfailures

Флаг (опция) командной строки, где n - это количество перезапусков
    "--reruns n"
Если при повторных запусках тесты пройдут успешно,
то и прогон тестов будет считаться успешным
"""

import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")

def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#magic_link")