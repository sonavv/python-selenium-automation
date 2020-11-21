from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, Then


@given('Open Amazon main page')
def open_Amazon(context):
    context.app.main_page.open_amazon()

@when('select Appliances department')
def select_appliances_dept(context):
    context.app.Dept_page.select_appliances_dept()

@then('Search for Kettle')
def input_search_word(context):
    context.app.Dept_page.input_search_word('Kettle')


@then('Verify Appliances department is selected')
def verify_dept_appliances_selected(context):
    context.app.Dept_page.verify_dept_appliances_selected()