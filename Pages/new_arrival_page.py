from Pages.base_page_reference import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

class NewArrival(Page):
    ARRIVAL_TAB =(By.CSS_SELECTOR, "a[href*='UTF8&bbn=17020138011&ie=UTF8&qid=1498592471&rh']")
    DEALS_LINK = (By.CSS_SELECTOR, "div.mega-menu")


    def open_Amazon(self):
        self.open_page('https://www.amazon.com/gp/product/B074TBCSC8')

    def hover_new_arrivals(self):
        arrival_tab = self.find_element(*self.ARRIVAL_TAB)
        actions = ActionChains(self.driver)
        actions.move_to_element(arrival_tab).perform()

    def verify_deals(self):
        self.wait_for_element_appear(*self.DEALS_LINK)