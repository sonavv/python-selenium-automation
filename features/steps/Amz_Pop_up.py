from selenium.webdriver.common.by import By
from behave import when, then, given
from selenium.webdriver.support import expected_conditions as EC

SIGN_IN_POPUP = (By.CSS_SELECTOR, "div.nav-signin-tooltip-footer")

@given("Open Amazon")
def open_page(context):
    context.driver.get('https://www.amazon.com')

@then("Sign-In popup is present and clickable")
def check_popup(context):
    context.driver.wait.until(EC.presence_of_element_located(SIGN_IN_POPUP))
    context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_POPUP))

@when("Sign_In popup disappears")
def popup_disappears(context):
    context.driver.wait.until(EC.invisibility_of_element(SIGN_IN_POPUP))

@then("Verify Sign-In popup is not clickable")
def popup_not_clickable(context):
    context.driver.wait.until_not(EC.element_to_be_clickable(SIGN_IN_POPUP))