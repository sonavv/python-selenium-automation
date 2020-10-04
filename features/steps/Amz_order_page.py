from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then

@given('Open Amazon home page')
def open_homepage(context):
    context.driver.get('https://www.amazon.com')

@when('click the order button')
def click_search_icon(context):
    search_icon = context.driver.find_element(By.XPATH, "//span[text()= '& Orders']")
    search_icon.click()

@then('sign in page has to open')
def verify_result(context):
    assert context.driver.find_element(By.XPATH, "//input[@id = 'ap_email']")
