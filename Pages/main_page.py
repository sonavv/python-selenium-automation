from Pages.base_page_reference import Page
from selenium.webdriver.common.by import By

class MainPage(Page):
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.XPATH, "//input[@value='Go']")


    def open_amazon(self):
        self.open_page('https://www.Amazon.com/')

    def input_search_word(self, text, *locator):
        self.input('Dress', *self.SEARCH_INPUT)
        """self.driver.find_element(*self.SEARCH_INPUT).send_keys('Dress')"""

    def click_search_icon(self):
        self.click(*self.SEARCH_ICON)
