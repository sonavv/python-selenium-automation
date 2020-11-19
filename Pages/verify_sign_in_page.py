from Pages.base_page_reference import Page
from selenium.webdriver.common.by import By

class SignInPage(Page):
    SEARCH_CLICK = (By.XPATH, "//span[text()= '& Orders']")
    SIGN_IN = (By.CSS_SELECTOR, "div.a-padding-extra-large h1.a-spacing-small")

    def click_icon(self):
        self.click(*self.SEARCH_CLICK)

    def verify_text(self, expected_text: str):
        actual_text = self.driver.find_element(*self.SIGN_IN).text
        assert expected_text == actual_text, f'Expected text {expected_text}, but got {actual_text}'