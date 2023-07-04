from selenium.webdriver.common.by import By

from web_tests.pages.base_page import BasePage


class InventoryPage(BasePage):

    def __init__(self, driver, tab_type):
        super().__init__(driver)
        self.tab_type = tab_type

    @property
    def inventory_container(self):
        return self.element((By.ID, self.tab_type[1]))

    def is_element_displayed(self):
        return self.inventory_container.is_displayed()