from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


driver=webdriver.Chrome(options=options)

driver.maximize_window()

driver.get('https://web.whatsapp.com/')



time.sleep(30)

# enter your number here
num=[ ]

# enter your Message
msg=" "

for z in num:
    driver.get(f'https://web.whatsapp.com/send/?phone={z}&text={msg}')
    time.sleep(15)
    action=ActionChains(driver)
    action.send_keys(Keys.ENTER)
    action.perform()
    time.sleep(5)
    
    
