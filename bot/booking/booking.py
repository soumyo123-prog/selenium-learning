# pylint: disable-all

import booking.constants as constants
from selenium import webdriver
import os

class Booking(webdriver.Chrome):
  def __init__(
    self, 
    driver_path = constants.DRIVER_PATH_LINUX, 
    teardown = False
  ):
    self.driver_path = driver_path
    self.teardown = teardown
    os.environ['PATH'] += self.driver_path
    super(Booking, self).__init__()
    self.implicitly_wait(15)

  def __exit__(self, *args):
    if (self.teardown):
      self.quit()

  def land_first_page(self):
    self.get(constants.BASE_URL)

  def change_currency(self, currency = None):
    currency_celement = (
      self.find_element_by_css_selector(
      'button[data-tooltip-text="Choose your currency"]'))
    currency_celement.click()
    selected_currency_element = (
      self.find_element_by_css_selector(
        f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'))
    selected_currency_element.click()

  def enter_place(self, place = None):
    search_field_element = self.find_element_by_id('ss')
    search_field_element.clear()
    search_field_element.send_keys(place)

    first_result = self.find_element_by_css_selector(
      'li[data-i="0"]')
    first_result.click()

  def select_dates(self, check_in, check_out):
    check_in_element = self.find_element_by_css_selector(
      f'td[data-date="{check_in}"]')
    check_in_element.click()
    check_out_element = self.find_element_by_css_selector(
      f'td[data-date="{check_out}"]')
    check_out_element.click()

  def select_guests(self, adult = 1, children = 0, room = 1):
    toggle_element = self.find_element_by_id('xp__guests__toggle')
    toggle_element.click()
    self.select_adults(adult)
    self.select_children(children)
    self.select_room(room)

  def select_adults(self, adult):
    decrease_adult = self.find_element_by_css_selector(
      'button[aria-label="Decrease number of Adults"]')
    increase_adult = self.find_element_by_css_selector(
      'button[aria-label="Increase number of Adults"]')
    adults = self.find_element_by_id('group_adults')
    adults_value = int(adults.get_attribute('value'))

    while (adults_value > 1):
      decrease_adult.click()
      adults_value = int(adults.get_attribute('value'))

    while (adults_value < adult):
      increase_adult.click()
      adults_value += 1

  def select_children(self, children):
    increase_children = self.find_element_by_css_selector(
      'button[aria-label="Increase number of Children"]')
    Children = self.find_element_by_id('group_children')
    children_value = int(Children.get_attribute('value'))

    while (children_value < children):
      increase_children.click()
      children_value += 1
  
  def select_room(self, room):
    increase_room = self.find_element_by_css_selector(
      'button[aria-label="Increase number of Rooms"]')
    rooms = self.find_element_by_id('no_rooms')
    rooms_value = int(rooms.get_attribute('value'))

    while (rooms_value < room):
      increase_room.click()
      rooms_value += 1

  def click_search(self):
    search_button = self.find_element_by_css_selector(
      'button[type="submit"]')
    search_button.click()