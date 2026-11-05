import pytest
from selene import browser, have


@pytest.fixture
def browser_open(scope='session'): #
    browser.open('https://github.com/search')


@pytest.fixture
def browser_chrome_setup_size(browser_open):
    browser.config.browser_name = 'chrome'
    browser.config.window_width = 1024
    browser.config.window_height = 768
    