from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):

    def should_thanks_for_registering_message(self):
        assert self.is_element_present(*MainPageLocators.THANKS_FOR_REGISTERING_MASSAGE), "MASSAGE is not presented"