from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

SEARCH_RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
SIGN_IN_BTN = (By.CSS_SELECTOR, '#nav-signin-tooltip > a')


@given('Open Amazon page')
def open_Amazon(context):
    context.app.main_page.open_amazon()


@when('Input Dress into Amazon search field')
def input_search_word(context):
    context.app.main_page.input_search_word('Dress')


@when('Click on Amazon Search icon')
def click_search_icon(context):
    context.app.main_page.click_search_icon()



@then('Search result Dress is shown')
def verify_search_result(context):
    context.app.search_result_page.verify_search_result('"Dress"')

@then('Verify Sign In is Clickable')
def verify_sign_in_clickable(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_BTN))


@then('Verify Sign In disappears')
def verify_sign_in_disappears(context):
    context.driver.wait.until(EC.invisibility_of_element_located(SIGN_IN_BTN))

@when('Wait for {sec} sec')
def sleep_sec(context, sec):
    sleep(int(sec))
