from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # ожидание подходящей цены
    price = WebDriverWait(browser, 60).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100')
    )

    # нажимаем на кнопку Book
    button = browser.find_element_by_id('book')
    button.click()

    # получаем число и вызываем функцию с этим числом для получения итогового значения
    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    y = calc(x)

    # пеередаем итоговое значение в поле input
    input = browser.find_element_by_css_selector('#answer')
    input.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element_by_id('solve')
    button.click()


finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
