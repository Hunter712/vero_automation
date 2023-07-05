from web_tests.pages.post_midview import PostMidviewPage
from web_tests.pages.profile_page import ProfilePage
import time
import pyperclip


def test_profile_tabs(driver, tabs_with_elements_inside, three_dots, copy_link):
    """
    1. Open user profile
    2. Navigate through the tabs on profile
    3. Verify that tabs clickable, posts exist for each tab(checking photo, video and music)
    """
    for tab in tabs_with_elements_inside:
        profile_page = ProfilePage(driver, tab, three_dots, copy_link)
        profile_page.navigate_to_profile_page()
        is_element_on_page = profile_page.click_on_tab()
        assert is_element_on_page.is_element_displayed()


def test_photo_switching(driver, photo_tab_and_post, three_dots, copy_link, arrows_on_post_midview, comments_button):
    """
    1. Open user profile
    2. Open any album post in photo tab
    3. Tap on left/right arrow to switch to the next photo
    4. Verify that arrows are clickable, photos load fine
    """
    profile_page = ProfilePage(driver, photo_tab_and_post, three_dots, copy_link)
    profile_page.navigate_to_profile_page()
    is_element_on_page = profile_page.click_on_tab()
    assert is_element_on_page.is_element_displayed()

    post_midview = PostMidviewPage(driver, photo_tab_and_post, arrows_on_post_midview, comments_button)
    post_midview.click_certain_post()
    #time.sleep(1)
    post_midview.click_on_right_arrow()
    #time.sleep(1)
    post_midview.click_on_right_arrow()
    #time.sleep(1)
    post_midview.click_on_left_arrow()
    #time.sleep(1)


def test_comments_for_post(driver, movie_tab_and_post, three_dots, copy_link, arrows_on_post_midview,
                           comments_button):
    """
    1. Open user profile
    2. Open any post in any tab
    3. Open comments window
    4. Verify that comments for post appeared
    """
    profile_page = ProfilePage(driver, movie_tab_and_post, three_dots, copy_link)
    profile_page.navigate_to_profile_page()
    is_element_on_page = profile_page.click_on_tab()
    assert is_element_on_page.is_element_displayed()

    post_midview = PostMidviewPage(driver, movie_tab_and_post, arrows_on_post_midview, comments_button)
    post_midview.click_certain_post()
    # time.sleep(1)
    is_element_on_page = post_midview.click_comments_button()
    # time.sleep(1)
    assert is_element_on_page.is_element_displayed()


def test_copied_profile_link(driver, movie_tab_and_post, three_dots, copy_link):
    """
    1. Open user profile
    2. Tap on 3 dots
    3. Tap on Copy link button
    4. Verify that copied link is right
    """
    profile_page = ProfilePage(driver, movie_tab_and_post, three_dots, copy_link)
    profile_page.navigate_to_profile_page()
    # time.sleep(1)
    profile_page.copy_link_button()
    # time.sleep(1)
    is_right_link_copied = pyperclip.paste()
    assert is_right_link_copied == "https://vero.co/vladyslav_fedorchenko"
