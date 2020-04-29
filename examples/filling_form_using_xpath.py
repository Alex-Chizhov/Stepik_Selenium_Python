from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_xpath_form")

    input1 = browser.find_element_by_xpath("//input[@name='first_name']")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath("//input[@name='last_name']")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath("//input[contains(@class, 'city')]")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_xpath("//input[@id='country']")
    input4.send_keys("Russia")
    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла для систем UNIX/Linux