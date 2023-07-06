from selenium.webdriver.common.by import By

from web_tests.pages.base_page import BasePage
from web_tests.pages.check_element_on_page import IsElementOnPage
from web_tests.helpers.project_helper import *
from web_tests.pages.post_midview import PostMidviewPage


class ProfilePage(BasePage):

    def __init__(self, driver, tab_type):
        super().__init__(driver)
        self.tab_type = tab_type

    def navigate_to_profile_page(self):
        self.driver.get(get_base_url())

    def click_on_tab(self):
        self.element((By.ID, self.tab_type[0])).click()
        return IsElementOnPage(self.driver, self.tab_type[1], By.ID)

    def click_certain_post(self):
        self.element((By.ID, self.tab_type[1])).click()
        return PostMidviewPage(self.driver, self.tab_type)

    def copy_link_button(self):
        self.element((By.XPATH, get_locator('three_dots_button'))).click()
        self.element((By.XPATH, get_locator('copy_link_button'))).click()
