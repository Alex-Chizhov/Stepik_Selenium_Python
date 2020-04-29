from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:

    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # клик по кнопке
    button1 = browser.find_element_by_css_selector("button.btn")
    button1.click()

    # переключаемся на всплывающее окно
    confirm = browser.switch_to.alert
    confirm.accept()

    # получаем число и вызываем функцию с этим числом для получения итогового значения
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    # вводим игоговое значение в input
    input = browser.find_element_by_id('answer')
    input.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
