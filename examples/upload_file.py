from selenium import webdriver
import time
import os

try:
    # получаем путь до файла в текущей директории
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла


    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # заполняем поля input(ов)
    first_name = browser.find_element_by_name('firstname')
    first_name.send_keys('Тест')
    last_name = browser.find_element_by_name('lastname')
    last_name.send_keys('Тест')
    email = browser.find_element_by_name('email')
    email.send_keys('Тест')

    # прикрепляем файл
    file_input = browser.find_element_by_name('file')
    file_input.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
