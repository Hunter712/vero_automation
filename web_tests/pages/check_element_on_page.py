from selenium.webdriver.common.by import By

from web_tests.pages.base_page import BasePage


class IsElementOnPage(BasePage):

    def __init__(self, driver, locator, locator_type):
        super().__init__(driver)
        self.locator = locator
        self.locator_type = locator_type

    @property
    def element_container(self):
        return self.element((self.locator_type, self.locator))

    def is_element_displayed(self):
        return self.element_container.is_displayed()