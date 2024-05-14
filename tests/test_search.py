"""
These tests cover DuckDuckGo searches
"""

from pages.search import DuckDuckGoSearchPage
from pages.result import DuckDuckGoResultPage


def test_basic_duckduckgo_search(browser):
    # Here we use the browser we get from the fixture to construct the two different pages 
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)
    PHRASE = "Panda"
    
    # Given the duckduckgo homepage is displayed
    search_page.load()

    # When the user searched for "panda"
    search_page.search(PHRASE)

    # Then the seach result title contains "panda"
    assert PHRASE in result_page.title()

    # And the search result query is "panda"
    assert PHRASE == result_page.search_input_value()

    # And the search result links pertain to "panda"
    titles = result_page.result_link_titles()
    matches = [t for t in titles if PHRASE.lower() in t.lower()]
    assert len(matches) > 0

    # TODO remove this exception once the test case is complete
    raise Exception("Incomplete Test")