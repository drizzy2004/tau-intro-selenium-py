"""
These tests cover DuckDuckGo searches
"""

import pytest
from pages.search import DuckDuckGoSearchPage
from pages.result import DuckDuckGoResultPage

@pytest.mark.parametrize('phrase', ['panda', 'python', 'polar bear'])
def test_basic_duckduckgo_search(browser, phrase):
    # Here we use the browser we get from the fixture to construct the two different pages 
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)
    
    # Given the duckduckgo homepage is displayed
    search_page.load()

    # When the user searched for the phrase
    search_page.search(phrase)

    # And the search result query is the phrase
    assert phrase == result_page.search_input_value()

    # And the search result links pertain to the phrase
    titles = result_page.result_link_titles()
    matches = [t for t in titles if phrase.lower() in t.lower()]
    assert len(matches) > 0

    # Then the seach result title contains the phrase
    # from selenium.webdriver.support.ui import WebDriverWait
    # from selenium.webdriver.support import expected_conditions as EC
    # WebDriverWait(driver, 10).until(EC.title_contains(PHRASE))
    assert phrase in result_page.title()