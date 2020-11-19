from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then



@given("Open Amazon Homepage")
def open_Amazon(context):
    context.app.main_page.open_amazon()

@when('click the cart icon')
def click_search_icon(context):
    context.app.verify_cart_page.click_search_icon()

@then('Verify the page shows Your Amazon Cart is empty')
def verify_search_result(context):
    context.app.verify_cart_page.verify_link('Your Amazon Cart is empty')


