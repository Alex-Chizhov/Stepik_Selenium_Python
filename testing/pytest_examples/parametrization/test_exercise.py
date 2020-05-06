import time
import math
import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(20)
    yield browser
    browser.quit()

links_list = [
'https://stepik.org/lesson/236895/step/1',
'https://stepik.org/lesson/236896/step/1',
'https://stepik.org/lesson/236897/step/1',
'https://stepik.org/lesson/236898/step/1',
'https://stepik.org/lesson/236899/step/1',
'https://stepik.org/lesson/236903/step/1',
'https://stepik.org/lesson/236904/step/1',
'https://stepik.org/lesson/236905/step/1'
]

@pytest.mark.parametrize('link', links_list)
def test_guest_should_see_login_link(browser, link):
    browser.get(link)
    textarea = browser.find_element_by_css_selector("textarea")
    textarea.send_keys(str(math.log(int(time.time()))))
    button_submit = browser.find_element_by_css_selector(".submit-submission")
    button_submit.click()
    answer = browser.find_element_by_css_selector(".smart-hints__hint").text
    assert answer == 'Correct!', f"Ответ не соответствует 'Correct!', ответ = {answer}"

