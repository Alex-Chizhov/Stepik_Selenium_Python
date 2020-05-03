"""
Если нужно проверить, что тест вызывает ожидаемое исключение (довольно редкая ситуация для UI-тестов,
и вам этот способ, скорее всего, никогда не пригодится),
мы можем использовать специальную конструкцию with pytest.raises().
Например, можно проверить, что на странице сайта не должен отображаться какой-то элемент:

В первом тесте элемент будет найден, поэтому ошибка NoSuchElementException,
которую ожидает контекстный менеджер pytest.raises, не возникнет, и тест упадёт.

Во втором тесте, как мы и ожидали, кнопка не будет найдена, и тест пройдет.
"""

import pytest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def test_exception1():
    try:
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/")
        with pytest.raises(NoSuchElementException):
            browser.find_element_by_css_selector("button.btn")
            pytest.fail("Не должно быть кнопки Отправить")
    finally:
        browser.quit()

def test_exception2():
    try:
        browser = webdriver.Chrome()
        browser.get("http://selenium1py.pythonanywhere.com/")
        with pytest.raises(NoSuchElementException):
            browser.find_element_by_css_selector("no_such_button.btn")
            pytest.fail("Не должно быть кнопки Отправить")
    finally:
        browser.quit()