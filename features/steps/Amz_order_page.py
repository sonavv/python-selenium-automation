from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then



@given('Open Amazon home page')
def open_homepage(context):
    context.app.main_page.open_amazon()

@when('click the order button')
def click_icon(context):
    context.app.verify_sign_in_page.click_icon()

"""def click_search_icon(context):
    search_icon = context.driver.find_element(*SEARCH_CLICK)
    search_icon.click()"""

@then('sign in page has to open')
def verify_search_result(context):
    context.app.verify_sign_in_page.verify_text('Sign-In')

"""def verify_result(context):
        context.app.search_result_page.verify_link('Sign-In')"""
