import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from web_tests.helpers.project_helper import *


@pytest.fixture()
def driver():
    browser_name = get_browser_name()
    if browser_name.lower() == 'chrome':
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser_name.lower() == 'firefox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise ValueError("Unknown browser")

    driver.maximize_window()
    driver.implicitly_wait(5)

    yield driver

    driver.quit()


@pytest.fixture()
def tabs_with_elements_inside():
    return [(get_locator('photo'), get_locator('local_photo_in_photo_tab')),
            (get_locator('video'), get_locator('local_video_in_video_tab')),
            (get_locator('music'), get_locator('local_music_in_music_tab'))]


@pytest.fixture()
def movie_tab_and_post():
    return (get_locator('movie'),
            get_locator('local_movie_in_movie_tab'))

@pytest.fixture()
def photo_tab_and_post():
    return (get_locator('photo'),
            get_locator('local_photo_in_photo_tab'))

@pytest.fixture()
def comments_button():
    return (get_locator('comment_button'),
            get_locator('local_comment'))


@pytest.fixture()
def arrows_on_post_midview():
    return (get_locator('left_arrow_button'),
            get_locator('right_arrow_button'))


@pytest.fixture()
def three_dots():
    return get_locator('three_dots_button')


@pytest.fixture()
def copy_link():
    return get_locator('copy_link_button')
