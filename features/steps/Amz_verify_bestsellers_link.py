from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, Then

LINKS_SEARCH = (By.CSS_SELECTOR, "a[href*= 'ref=zg_bs_tab'")
TOP_LINKS = (By.CSS_SELECTOR, "#zg_tabs a")
HEADER = (By.CSS_SELECTOR, "#zg_banner_text_wrapper")

@given('Open the Best Sellers page in Amazon')
def open_page(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')

@then('Verify there are 5 links')
def check_links(context):
    link_count = len(context.driver.find_elements(*LINKS_SEARCH))
    assert link_count == 5, f'Error. Expected 5, but got {link_count}'

@then('User can click all the links on the top and verify it opens the correct page')
def click_top_links(context):
    top_links = context.driver.find_elements(*TOP_LINKS)

    for x in range(len(top_links)):
        top_links = context.driver.find_elements(*TOP_LINKS)
        link = top_links[x]
        link_text = link.text
        link.click()

        header_text = context.driver.find_element(*HEADER).text
        assert link_text in header_text, f"Expected {link_text} not in {header_text}"