from selenium.webdriver.common.by import By

from web_tests.pages.base_page import BasePage


class IsElementOnPage(BasePage):

    def __init__(self, driver, locator, locator_type):
        super().__init__(driver)
        self.locator = locator
        self.locator_type = locator_type

    @property
    def element_container(self):
        if self.locator_type == "id":
            return self.element((By.ID, self.locator))
        elif self.locator_type == "xpath":
            return self.element((By.XPATH, self.locator))

    def is_element_displayed(self):
        return self.element_container.is_displayed()