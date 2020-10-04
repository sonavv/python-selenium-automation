from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# init driver
driver = webdriver.Chrome(executable_path='C:\Program Files\Git\Automation\Automation\python-selenium-automation\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)

# open the url
driver.get('https://www.amazon.com/gp/help/customer/display.html')

input_field = driver.find_element(By.ID, 'helpsearch')
input_field.send_keys('cancel order')

search_icon = driver.find_element(By.XPATH, "//input[@id ='helpsearch']").send_keys(Keys.ENTER)


result1 = driver.find_element(By.XPATH, "//h1[text()= 'Cancel Items or Orders']")
assert result1.text == 'Cancel Items or Orders', f'Error. Expected Cancel Items or Orders, but got (result1.text)'
driver.quit()


