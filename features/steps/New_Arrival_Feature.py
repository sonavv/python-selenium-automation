from selenium.webdriver.common.by import By
from behave import given, when, then

@given('Open Amazon product page')
def open_Amazon(context):
    context.app.new_arrival_page.open_Amazon()

@when('Hover over New Arrivals tab')
def hover_new_arrivals(context):
    context.app.new_arrival_page.hover_new_arrivals()

@then('Verify the deals are shown')
def verify_deals(context):
    context.app.new_arrival_page.verify_deals()

