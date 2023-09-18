from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


driver=webdriver.Chrome(options=options)

driver.maximize_window()

driver.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

print('Selenium Easy Demo - Simple Form to Automate using Selenium' in driver.title)

fillbox = driver.find_element(By.ID, 'user-message')
fillbox.clear()
fillbox.send_keys('HOLAAAAAA')


button = driver.find_element(By.CLASS_NAME, 'btn-primary')
button.click()


time.sleep(10)

driver.close()
