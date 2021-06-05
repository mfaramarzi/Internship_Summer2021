import json
import random

class TestCase:
  """
  A Single Test Case for Booking A Room

  range - the number of rooms in the hotel (default 0)
  number - the number of booked rooms (default 0)
  rooms - a list of room numbers that are occupied (default empty)
  answer - the correct answer for the test case (default empty)
  """
  def __init__(self):
    self.range = random.randint(1, 100)
    self.number = random.randint(1, range)
    self.answer = ''

    if (range == self.number):
      self.answer = 'too late'
    
    self.rooms = []




  