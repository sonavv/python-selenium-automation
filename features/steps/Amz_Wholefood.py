from behave import given, then
from selenium.webdriver.common.by import By

PRODUCTS = (By.CSS_SELECTOR, "div#wfm-pmd_deals_section")

@given("Open Amazon Wholefood Page")
def open_wholefood(context):
    context.driver.get('https://www.amazon.com/wholefoodsdeals')

@then("Verify the products has regular price")
def check_products(context):
    all_products = context.driver.find_elements(*PRODUCTS)
    for products in all_products:
        assert "Regular" in products.text, f"Expected 'Regular' but got {products.text}"