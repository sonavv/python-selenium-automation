from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

COLOR_OPTIONS = (By.CSS_SELECTOR, '#variation_color_name li')
SELECTED_COLOR = (By.CSS_SELECTOR, '#variation_color_name span.selection')
PANT_COLORS_AVAILABLE = (By.CSS_SELECTOR, '#variation_color_name li')
PANT_COLOR_SELECTED = (By.CSS_SELECTOR, '#variation_color_name span.selection')

@given('Open Amazon Dress {productid} page')
def open_dress_page(context, productid):
    context.driver.get(f'https://www.amazon.com/gp/product/{productid}/')


@then('Verify user can select through colors')
def verify_dress_colors(context):
    expected_colors = ['Emerald', 'Ivory','Navy']
    colors = context.driver.find_elements(*COLOR_OPTIONS)

    #for i in range(len(colors)):
        #colors[i].click()
        #colors_text = context.driver.find_element(*SELECTED_COLOR).text
        #assert colors_text == expected_colors[i], \
         #   f"color dont match. Expected{expected_colors[i]} but got got {colors_text}"

    #for color in colors:
       # color.click()
       # assert context.driver.find_element(*SELECTED_COLOR).text != ''

    for color in colors:
        color.click()
        context.driver.wait.until(EC.url_changes, "url did not change")

@given('Open Amazon mens fashion {itemid} page')
def open_fashion_page(context, itemid):
    context.driver.get(f'https://www.amazon.com/gp/product/{itemid}/')

@then('Verify user can select through pant colors')
def verify_pant_color(context):
    expected_pant_color = ['Black', 'Blue Overdyed', 'Dark Wash', \
                           'Indigo Wash', 'Light Wash', 'Medium Wash', \
                           'Rinse', 'Vintage Light Wash']
    pant_colors = context.driver.find_elements(*PANT_COLORS_AVAILABLE)

    for i in range(len(pant_colors)):
        pant_colors[i].click()
        colors_text = context.driver.find_element(*PANT_COLOR_SELECTED).text
        assert colors_text == expected_pant_color[i], \
            f"color dont match. Expected{expected_pant_color[i]} \ " \
            f"but got got {colors_text}"
