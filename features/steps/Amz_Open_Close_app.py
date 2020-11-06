from selenium.webdriver.common.by import By
from behave import when, then, given
from selenium.webdriver.support import expected_conditions as EC

LINK = (By.XPATH, "//a[contains(@href,'docId=1000625601')]")
AMAZON_APP_LINK = (By.CSS_SELECTOR, "div.a-container  .amabot_center")

@given('Open Amazon T&C page')
def open_tc_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')

@then('Click on Amazon applications link')
def click_link(context):
    context.home_windows = context.driver.window_handles
    context.home_window = context.driver.current_window_handle
    link = context.driver.find_element(*LINK)
    link.click()
    print(context.home_windows)
    print(context.home_window)

@when('Switch to the newly opened window')
def switch_windows(context):
    context.driver.wait.until(EC.new_window_is_opened)
    new_windows = context.driver.window_handles
    print(new_windows)
    for window in context.home_windows:
        new_windows.remove(window)
    print(new_windows)
    context.driver.switch_to_window(new_windows[0])

@then('Amazon app page is opened')
def check_website_name(context):
    context.driver.find_element(*AMAZON_APP_LINK)

@then("User can close new window and switch back to original")
def go_back(context):
    context.driver.close()
    context.driver.switch_to_window(context.home_window)