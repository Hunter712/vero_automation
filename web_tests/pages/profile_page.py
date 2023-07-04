from selenium.webdriver.common.by import By

from web_tests.helpers.project_helper import get_base_url
from web_tests.pages.base_page import BasePage
from web_tests.pages.inventory_page import InventoryPage
import time


class ProfilePage(BasePage):

    def __init__(self, driver, tab_type):
        super().__init__(driver)
        self.tab_type = tab_type

    def navigation_to_profile_page(self):
        self.driver.get(get_base_url())

    @property
    def photo_tab(self):
        return self.element((By.ID, self.tab_type[0]))

    def click_on_tab(self):
        self.photo_tab.click()
        return InventoryPage(self.driver, self.tab_type)
