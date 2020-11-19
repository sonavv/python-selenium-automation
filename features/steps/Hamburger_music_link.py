from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, Then


@given('Open Amazon Page to Find Hamburger Icon')
def open_Amazon(context):
    context.app.main_page.open_amazon()

@when('Click hamburger menu icon')
def click_search_icon(context):
    context.app.Hamburger_page.click_search_icon()

@then('Click Amazon Music from the menu')
def find_element(context):
    context.app.Hamburger_page.find_element()

@then('Verify there are 7 items in the menu')
def verify_items_in_menu(context):
    context.app.Hamburger_page.verify_items_in_menu(7)

"""def check_links(context):
    menu_count = len(context.driver.find_elements(*MENU_ITEMS))
    assert menu_count == 7, f'Error. Expected 7, but got {menu_count}'"""