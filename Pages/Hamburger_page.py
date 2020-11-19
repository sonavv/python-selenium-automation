from Pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Hamburger(Page):
    HAMBURGER_ICON = (By.CSS_SELECTOR, "#nav-hamburger-menu")
    AMAZON_MUSIC = (By.XPATH, "//ul[contains(@class, 'hmenu-visible')] // div[contains(text(), 'Amazon Music')]")
    MENU_ITEMS = (By.CSS_SELECTOR, "ul.hmenu-translateX a[class=hmenu-item]")

    def click_search_icon(self):
        self.click(*self.HAMBURGER_ICON)

    def find_element(self):
        self.driver.find_element(*self.AMAZON_MUSIC).click()

    def verify_items_in_menu(self, item_count: int):
        self.driver.wait.until(
            lambda driver: len(driver.find_elements(*self.MENU_ITEMS))== item_count,
            f'Number of items did not match expected {item_count}'
        )

