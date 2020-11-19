from Pages.base_page import Page
from selenium.webdriver.common.by import By

class SearchResult(Page):
    """Xpath for searching item in amazon(eg dress) (for amazon_search feature file)"""
    SEARCH_RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")


    def verify_search_result(self, expected_text):
        self.verify_text(expected_text, *self.SEARCH_RESULT)
