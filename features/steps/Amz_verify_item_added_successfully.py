from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, Then

SEARCH_ITEM = (By.CSS_SELECTOR, "input#twotabsearchtextbox")
SEARCH_BTN1 = (By.CSS_SELECTOR, "input[value = Go]")
ADD_TO_CART = (By.XPATH, "//input[@id = 'add-to-cart-button']")
CHECK_CART = (By.XPATH, "//a[@id='hlb-ptc-btn-native']")

@given("Open Amazon frontpage")
def open_amazon_homepage(context):
    context.driver.get("https://www.amazon.com/")

@when('Input vase into amazon search')
def search_box(context):
    search_b = context.driver.find_element(*SEARCH_ITEM).send_keys('Vase')

@Then('Click on the search icon')
def click_search_icon(context):
    click_search_btn = context.driver.find_element(*SEARCH_BTN1)
    click_search_btn.click()

@Then('Add the first item to the cart')
def add_item1(context):
    item1 = context.driver.find_element(By.XPATH, "//span[@class='a-size-base-plus a-color-base a-text-normal' and text()= 'Libbey Prologue Drift Handmade Ceramic Carafe Vase, White']")
    item1.click()

@Then('click on the add icon')
def add_to_cart(context):
    add_cart = context.driver.find_element(*ADD_TO_CART)
    add_cart.click()

@Then('verify the cart has the item')
def verify_cart(context):
    verify_cart1 = context.driver.find_element(*CHECK_CART)



