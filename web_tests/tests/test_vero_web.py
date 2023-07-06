import pytest

from web_tests.pages.profile_page import ProfilePage
from web_tests.helpers.project_helper import *
import time
import pyperclip


@pytest.mark.parametrize("tab",
                         [(get_locator('photo'), get_locator('local_photo_in_photo_tab')),
                          (get_locator('video'), get_locator('local_video_in_video_tab')),
                          (get_locator('music'), get_locator('local_music_in_music_tab'))])
def test_profile_tabs(driver, tab):
    """
    1. Open user profile
    2. Navigate through the tabs on profile
    3. Verify that tabs clickable, posts exist for each tab(checking photo, video and music)
    """
    profile_page = ProfilePage(driver, tab)
    profile_page.navigate_to_profile_page()
    # time.sleep(1)
    is_element_on_page = profile_page.click_on_tab()
    assert is_element_on_page.is_element_displayed()
    # time.sleep(1)


@pytest.mark.parametrize("tab",
                         [(get_locator('photo'), get_locator('local_photo_in_photo_tab'))
                          # (get_locator('video'), get_locator('local_video_in_video_tab')),
                          # (get_locator('music'), get_locator('local_music_in_music_tab'))
                          ])
def test_photo_switching(driver, tab):
    """
    1. Open user profile
    2. Open any album post in photo tab
    3. Tap on left/right arrow to switch to the next photo
    4. Verify that arrows are clickable, photos load fine
    """
    profile_page = ProfilePage(driver, tab)
    profile_page.navigate_to_profile_page()
    is_element_on_page = profile_page.click_on_tab()
    assert is_element_on_page.is_element_displayed()

    post_midview = profile_page.click_certain_post()
    # time.sleep(1)
    post_midview.click_on_right_arrow()
    # time.sleep(1)
    post_midview.click_on_right_arrow()
    # time.sleep(1)
    is_element_on_page = post_midview.click_on_left_arrow()
    # time.sleep(1)
    assert is_element_on_page.is_element_displayed()


@pytest.mark.parametrize("tab",
                         [(get_locator('movie'), get_locator('local_movie_in_movie_tab'))
                          # (get_locator('photo'), get_locator('local_photo_in_photo_tab'))
                          # (get_locator('video'), get_locator('local_video_in_video_tab')),
                          # (get_locator('music'), get_locator('local_music_in_music_tab'))
                          ])
def test_comments_for_post(driver, tab):
    """
    1. Open user profile
    2. Open any post in any tab
    3. Open comments window
    4. Verify that comments for post appeared
    """
    profile_page = ProfilePage(driver, tab)
    profile_page.navigate_to_profile_page()
    is_element_on_page = profile_page.click_on_tab()
    assert is_element_on_page.is_element_displayed()

    post_midview = profile_page.click_certain_post()
    # time.sleep(1)
    is_element_on_page = post_midview.click_comments_button()
    # time.sleep(1)
    assert is_element_on_page.is_element_displayed()


@pytest.mark.parametrize("tab",
                         [(get_locator('movie'), get_locator('local_movie_in_movie_tab'))
                          # (get_locator('photo'), get_locator('local_photo_in_photo_tab'))
                          # (get_locator('video'), get_locator('local_video_in_video_tab')),
                          # (get_locator('music'), get_locator('local_music_in_music_tab'))
                          ])
def test_copied_profile_link(driver, tab):
    """
    1. Open user profile
    2. Tap on 3 dots
    3. Tap on Copy link button
    4. Verify that copied link is right
    """
    profile_page = ProfilePage(driver, tab)
    profile_page.navigate_to_profile_page()
    # time.sleep(1)
    profile_page.copy_link_button()
    # time.sleep(1)
    is_right_link_copied = pyperclip.paste()
    assert is_right_link_copied == "https://vero.co/vladyslav_fedorchenko"
