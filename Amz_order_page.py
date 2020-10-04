from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# init driver
driver = webdriver.Chrome(executable_path='C:\Program Files\Git\Automation\Automation\python-selenium-automation\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)

# open the url
driver.get('https://www.amazon.com')
search_icon = driver.find_element(By.XPATH, "//span[text()= '& Orders']")
search_icon.click()

assert driver.find_element(By.XPATH, "//input[@id = 'ap_email']")

driver.quit()

