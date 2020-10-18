from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, Then

LINKS_SEARCH = (By.CSS_SELECTOR, "a[href*= 'ref=zg_bs_tab'")

@given('Open the Best Sellers page in Amazon')
def open_page(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')

@Then('Verify there are 5 links')
def check_links(context):
    link_count = len(context.driver.find_elements(*LINKS_SEARCH))
    assert link_count == 5, f'Error. Expected 5, but got {link_count}'

