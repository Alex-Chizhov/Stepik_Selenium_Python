from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # получаем число и вызываем функцию с этим числом для получения итогового значения
    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    y = calc(x)

    # пеередаем итоговое значение в поле input
    input = browser.find_element_by_css_selector('#answer')
    input.send_keys(y)

    # прокручиваем страницу вниз на 100px
    # browser.execute_script("window.scrollBy(0, 100);")


    # отмечаем checkbox и radiobutton
    checkbox = browser.find_element_by_css_selector('#robotCheckbox')
    checkbox.click()

    # прокручиваем страницу чтобы radiobutton был в начале страницы метод 1
    # button = browser.find_element_by_tag_name("button")
    # browser.execute_script("return arguments[0].scrollIntoView({block: 'start'});", button)
    # button.click()

    # прокручиваем страницу чтобы radiobutton был в начале страницы метод 2
    browser.execute_script("""  
                radiobutton = document.getElementById('robotsRule');
                radiobutton.scrollIntoView({block: 'start'});
    """)
    radiobutton = browser.find_element_by_css_selector('#robotsRule')
    radiobutton.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
