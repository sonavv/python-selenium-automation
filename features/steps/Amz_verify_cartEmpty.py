from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then

@given("Open Amazon Homepage")
def open_amazon_homepage(context):
    context.driver.get("https://www.amazon.com/")

@when('click the cart icon')
def click_icon(context):
    cart = context.driver.find_element(By.XPATH, "//span[@id='nav-cart-count']")
    cart.click()

@then('Verify the page shows Your Amazon Cart is empty')
def verify_cart(context):
    res = context.driver.find_element(By.CSS_SELECTOR, ("div.sc-your-amazon-cart-is-empty"))
    assert res.text == 'Your Amazon Cart is empty', f'Error. Expected Your Amazon Cart is empty, but got {res.text}'


