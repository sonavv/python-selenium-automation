from Pages.base_page_reference import Page
from selenium.webdriver.common.by import By

class EmptyCart(Page):
    CART_ICON = (By.XPATH, "//span[@id='nav-cart-count']")
    VERIFY_CART = (By.CSS_SELECTOR, ("div.sc-your-amazon-cart-is-empty"))

    def click_search_icon(self):
        self.click(*self.CART_ICON)

    def verify_link(self, expected: str):
        actual_text = self.driver.find_element(*self.VERIFY_CART).text
        assert expected == actual_text, f'Expected text {expected}, but got {actual_text}'
