from Pages.base_page_reference import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class DeptPage(Page):
    DEPT_APPLIANCES = (By.ID, 'searchDropdownBox')
    ITEM_TO_FIND = (By.ID, 'twotabsearchtextbox')
    CURRENT_CATEGORY = (By.XPATH, "//span[text() = 'Appliances']")

    def select_appliances_dept(self):
        da = self.find_element(*self.DEPT_APPLIANCES)
        select = Select(da)
        select.select_by_value('search-alias=appliances')

    def input_search_word(self, text, *locator):
        self.input('Kettle', *self.ITEM_TO_FIND)

    def verify_dept_appliances_selected(self):
        ca = self.wait_for_element_appear(*self.CURRENT_CATEGORY)
