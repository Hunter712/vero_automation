
from web_tests.pages.profile_page import ProfilePage
import time


def test_profile_tabs(driver, tabs_with_elements_inside):
    """
    1. Open user profile
    2. Navigate through the tabs on profile
    3. Verify that tabs clickable, posts exist for each tab(checking photo, video and music)
    """
    for tab in tabs_with_elements_inside:
        profile_page = ProfilePage(driver, tab)
        profile_page.navigation_to_profile_page()
        inventory_page = profile_page.click_on_tab()
        #time.sleep(1)
        assert inventory_page.is_element_displayed()
        #time.sleep(1)


