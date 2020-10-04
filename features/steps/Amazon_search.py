from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.XPATH, "//input[@value='Go']")
SEARCH_RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")

@given('Open Amazon page')
def open_Amazon(context):
    context.driver.get('https://www.Amazon.com/')


@when('Input Dress into Amazon search field')
def input_search(context):
    search = context.driver.find_element(*SEARCH_INPUT).send_keys('Dress')
    sleep(4)


@when('Click on Amazon Search icon')
def click_search_icon(context):
    search_icon = context.driver.find_element(*SEARCH_ICON)
    search_icon.click()



@then('Search result Dress is shown')
def verify_search_result(context):
    result = context.driver.find_element(*SEARCH_RESULT)
    assert result.text == '"Dress"', f'Error. Expected Dress, but got {result.text}'



