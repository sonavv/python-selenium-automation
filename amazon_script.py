from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='C:\Program Files\Git\Automation\Automation\python-selenium-automation\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)

# open the url
driver.get('https://www.Amazon.com/')

input_field = driver.find_element(By.ID, 'twotabsearchtextbox')
input_field.send_keys('Dress')

search_icon = driver.find_element(By.XPATH, "//input[@value='Go']")
search_icon.click()

result = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']")
assert result.text == '"Dress"', f'Error. Expected Dress, but got (result.text)'

driver.quit()


