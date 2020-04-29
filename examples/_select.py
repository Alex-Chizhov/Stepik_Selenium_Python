from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time

link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    # получаем числа и складываем их
    num1 = browser.find_element_by_css_selector('#num1').text
    num2 = browser.find_element_by_css_selector('#num2').text
    sum = int(num1) + int(num2)

    # выбираем из выпадающего списка нужный пунк
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(sum))


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
