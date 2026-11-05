import pytest
from selene import browser, have


def test_search_github(browser_chrome_setup_size,browser_open):
    browser.element('[aria-label="Search GitHub"]').type('qa.guru').press_enter()
    browser.element('[data-testid="results-list"]').should(have.text('QA.GURU'))

def test_search_returns_0_results(browser_chrome_setup_size,browser_open):
    browser.element('[aria-label="Search GitHub"]').type('првагшырпгшвыар425243524362').press_enter()
    browser.element('body').should(have.text('Your search did not match any repositories'))




