from selenium import webdriver

class Booking(webdriver.Chrome):
  def __init__(self, driver_path = r"C:/Users/deyso/WebDrivers"):
    self.driver_path = driver_path
    super(Booking, self).__init__()