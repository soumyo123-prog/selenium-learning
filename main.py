import os
from selenium import webdriver

os.system('export PATH="/home/spunky/selenium":$PATH')
driver = webdriver.Chrome()
driver.get('https://www.seleniumeasy.com/test/jquery-download-progress-bar-demo.html')

driver.implicitly_wait(5)
# We could have used time.sleep() here,
# but that would make us wait full 5 seconds even if the webpage is loaded
# hence we use implicitly_wait
# implicitly_wait is applied to all the elements we try to find

element = driver.find_element_by_id('downloadButton')
element.click()