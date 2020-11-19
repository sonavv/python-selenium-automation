from Pages.main_page import MainPage
from Pages.search_result_page import SearchResult
from Pages.verify_sign_in_page import SignInPage
from Pages.verify_cart_page import EmptyCart
from Pages.Hamburger_page import Hamburger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Application:
    def __init__(self, driver):
        self.driver = driver

        self.main_page = MainPage(self.driver)

        self.search_result_page = SearchResult(self.driver)

        self.verify_sign_in_page = SignInPage(self.driver)

        self.verify_cart_page = EmptyCart(self.driver)

        self.Hamburger_page = Hamburger(self.driver)