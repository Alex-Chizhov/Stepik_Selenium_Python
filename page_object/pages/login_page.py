from .base_page import BasePage
from .locators import LoginPageLocators
from ..tests_data import user_registration_data

class LoginPage(BasePage):

    def go_to_login_page(self):
        self.browser.get('http://selenium1py.pythonanywhere.com/en-gb/accounts/login/')

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert "login" in current_url, '"login" отсутствует в текущем URL'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self):
        user_data = user_registration_data()
        email = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        email.send_keys(user_data[0])
        password = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password.send_keys(user_data[1])
        password_confirm = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_INPUT)
        password_confirm.send_keys(user_data[1])
        register_button = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER)
        register_button.click()