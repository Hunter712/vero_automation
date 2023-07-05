import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from web_tests.helpers.project_helper import get_browser_name


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
    return [('filter-photo', 'post-t-88mzp2ShDzvmpSmgDvdL54'),
            ('filter-video', 'post-M3nF-2f4MBScbGs1XsfCV7fk'),
            ('filter-music', 'post-78-jKzDCNRPT31nj635jkW54')]


@pytest.fixture()
def movie_tab_and_post():
    return ('filter-movie',
            'post-7H-XDstff6xbwQ4dfPWRMRG9')

@pytest.fixture()
def photo_tab_and_post():
    return ('filter-photo',
            'post-rZ-LZCQVsZjgq1r3N2CkS59f')

@pytest.fixture()
def comments_button():
    return ('//div[@class="comments"]',
            "//div[@class='comment-content']/p/span[text() = '5']")


@pytest.fixture()
def arrows_on_post_midview():
    return ('//*[@id="rZ-LZCQVsZjgq1r3N2CkS59f"]/div[1]/div[1]/button[1]',
            '//*[@id="rZ-LZCQVsZjgq1r3N2CkS59f"]/div[1]/div[1]/button[2]')


@pytest.fixture()
def three_dots():
    return '//div[@class="options options-desktop"]'


@pytest.fixture()
def copy_link():
    return '//div[@class="modal-container options-menu"]/ul/li[4]'
