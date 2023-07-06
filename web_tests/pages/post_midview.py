from selenium.webdriver.common.by import By

from web_tests.pages.base_page import BasePage
from web_tests.pages.check_element_on_page import IsElementOnPage
from web_tests.helpers.project_helper import *


class PostMidviewPage(BasePage):

    def __init__(self, driver, tab_type):
        super().__init__(driver)
        self.tab_type = tab_type

    def click_comments_button(self):
        self.element((By.XPATH, get_locator('comment_button'))).click()
        return IsElementOnPage(self.driver, get_locator('local_comment'), By.XPATH)

    def click_on_right_arrow(self):
        self.element((By.XPATH, get_locator('right_arrow_button'))).click()

    def click_on_left_arrow(self):
        self.element((By.XPATH, get_locator('left_arrow_button'))).click()
        return IsElementOnPage(self.driver, get_locator('certain_image'), By.XPATH)

