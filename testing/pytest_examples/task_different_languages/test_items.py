import time

def test_check_button_add_to_cart(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    time.sleep(30)
    assert browser.find_element_by_css_selector('.btn-add-to-basket'), 'Кнопки с классом "btn-add-to-basket" нет'

