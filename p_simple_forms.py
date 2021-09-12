import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

os.environ['PATH'] += r';C:/Users/deyso/WebDrivers'
driver = webdriver.Chrome()
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
driver.implicitly_wait(5)

try:
  close_ad_button = driver.find_element_by_class_name('at-cm-no-button')
  close_ad_button.click()
except:
  print('No advertisement found')

sum_input_1 = driver.find_element_by_id('sum1')
sum_input_2 = driver.find_element_by_id('sum2')

sum_input_1.send_keys(Keys.NUMPAD1, Keys.NUMPAD0)
sum_input_2.send_keys(12)

submit_button = driver.find_element_by_css_selector('button[onclick="return total()"]')
submit_button.click()
