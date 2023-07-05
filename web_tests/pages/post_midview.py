from selenium.webdriver.common.by import By

from web_tests.pages.base_page import BasePage
from web_tests.pages.check_element_on_page import IsElementOnPage


class PostMidviewPage(BasePage):
    FIND_BY_ID = "id"
    FIND_BY_XPATH = "xpath"

    def __init__(self, driver, certain_tab_and_post, arrows_on_post_midview, comment_button):
        super().__init__(driver)
        self.arrows_on_post_midview = arrows_on_post_midview
        self.certain_tab_and_post = certain_tab_and_post
        self.comment_button = comment_button

    def click_certain_post(self):
        self.element((By.ID, self.certain_tab_and_post[1])).click()

    def click_comments_button(self):
        self.element((By.XPATH, self.comment_button[0])).click()
        return IsElementOnPage(self.driver, self.comment_button[1], PostMidviewPage.FIND_BY_XPATH)

    def click_on_right_arrow(self):
        self.element((By.XPATH, self.arrows_on_post_midview[1])).click()

    def click_on_left_arrow(self):
        self.element((By.XPATH, self.arrows_on_post_midview[0])).click()
