from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Page:
    def __init__(self, driver):
        self.driver = driver
        self.driver.wait = WebDriverWait(self.driver, 15)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def open_page(self, url):
        self.driver.get(url)

    def input(self, text: str, *locator):
        """
        Find input by locator and input text
        :param text: text to input
        :param locator: Search strategy and locator of web element (ex. (By.ID, 'id') )
        """
        e = self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text)

    """def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)"""

    def verify_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text == actual_text, f"Expected {expected_text} does not match the {actual_text}"

    def find_element(self, *locator):
        self.driver.find_element(*locator).click()