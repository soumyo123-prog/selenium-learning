import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

os.environ['PATH'] += r';C:/Users/deyso/WebDrivers'
driver = webdriver.Chrome()
driver.get('https://www.seleniumeasy.com/test/jquery-download-progress-bar-demo.html')

driver.implicitly_wait(5)
# We could have used time.sleep() here,
# but that would make us wait full 5 seconds even if the webpage is loaded
# hence we use implicitly_wait
# implicitly_wait is applied to all the elements we try to find

button_element = driver.find_element_by_id('downloadButton')
button_element.click()

WebDriverWait(driver, 30).until(
  EC.text_to_be_present_in_element(
    (By.CLASS_NAME, 'progress-label'), # Element Filteration 
    'Complete!' # Text to be found
  )
)
