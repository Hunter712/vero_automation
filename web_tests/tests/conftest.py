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