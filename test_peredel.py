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

def test_search_github(browser_chrome_setup_size,browser_open):
    browser.element('[aria-label="Search GitHub"]').type('qa.guru').press_enter()
    browser.element('[data-testid="results-list"]').should(have.text('QA.GURU'))

def test_search_returns_0_results(browser_chrome_setup_size,browser_open):
    browser.element('[aria-label="Search GitHub"]').type('првагшырпгшвыар425243524362').press_enter()
    browser.element('body').should(have.text('Your search did not match any repositories'))




