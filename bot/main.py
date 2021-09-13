# pylint: disable-all

from booking.booking import Booking

with Booking() as bot:
  bot.land_first_page()
  # bot.change_currency(currency = 'INR')
  bot.enter_place(place = 'New York')
  bot.select_dates(check_in = "2021-09-20", check_out = "2021-09-30")
  bot.select_guests(adult = 5, room = 2)
  bot.click_search()