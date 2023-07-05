from selenium.webdriver.common.by import By

from web_tests.helpers.project_helper import get_base_url
from web_tests.pages.base_page import BasePage
from web_tests.pages.check_element_on_page import IsElementOnPage


class ProfilePage(BasePage):
    FIND_BY_ID = "id"
    FIND_BY_XPATH = "xpath"

    def __init__(self, driver, tab_type, three_dots, copy_link):
        super().__init__(driver)
        self.tab_type = tab_type
        self.three_dots = three_dots
        self.copy_link = copy_link

    def navigate_to_profile_page(self):
        self.driver.get(get_base_url())

    def click_on_tab(self):
        self.element((By.ID, self.tab_type[0])).click()
        return IsElementOnPage(self.driver, self.tab_type[1], ProfilePage.FIND_BY_ID)

    def copy_link_button(self):
        self.element((By.XPATH, self.three_dots)).click()
        self.element((By.XPATH, self.copy_link)).click()
