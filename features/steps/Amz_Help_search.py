from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
from time import sleep

@given('Open Amazon help page')
def open_help(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')

@when('Input cancel order into help search field')
def input_helpsearch(context):
    search = context.driver.find_element(By.XPATH, "//input[@id ='helpsearch']").send_keys('cancel order')

@then('Press Enter on help Search icon')
def enter_search_icon(context):
    search_icon = context.driver.find_element(By.XPATH, "//input[@id ='helpsearch']").send_keys(Keys.ENTER)

@then('Search result Cancel Items or Orders  is shown')
def verify_search_result(context):
    result1 = context.driver.find_element(By.XPATH, "//h1[text()= 'Cancel Items or Orders']")
    assert result1.text == 'Cancel Items or Orders', f'Error. Expected Cancel Items or Orders, but got {result1.text}'





