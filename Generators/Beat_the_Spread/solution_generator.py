import json
import random

class TestCase:
  """
  A Single Test Case for Beat the Spread

  n - number of score spreads
  spreads - a list of tuples, representing the sum and absolute difference
  answers - a list of tuples, representing the correct answer for each line
  """
  def __init__(self):
    self.n = random.randint(1, 20)
    self.spreads = []
    self.answers = []

    i = 0
    while i < self.n:
      s = random.randint(0, 1000)
      d = random.randint(0, 1000)
      self.spreads.append((s, d))
      
      if (s < d) or ((s + d) % 2 == 1):
        self.answers.append('impossible')
      else:
        hi = (s + d) / 2
        lo = s - hi
        if (lo > hi):
          lo, hi = hi, lo
        self.answers.append((hi, lo))
      i += 1


def generate_case(case_number, case):
  new_case = {}

  new_case["case"] = case_number

  case_input = "%s\n" % (case.n)
  for i in range(case.n):
    next_input = "%s %s\n" % (case.spreads[i][0], case.spreads[i][1])
    case_input = case_input + next_input
  
  new_case["input"] = case_input

  case_output = ""
  for i in range(case.n):
    next_output = ""
    if (case.answers[i] == 'impossible'):
      next_output = 'impossible\n'
    else:
      next_output = "%s %s\n" % (case.answers[i][0], case.answers[i][1])
    case_output = case_output + next_output
  
  new_case["output"] = case_output

  return new_case


def generate_test_cases():
  test_cases = {}
  tests = []

  for i in range(50):
    case = TestCase()
    tests.append(generate_case(i + 1, case))
  
  test_cases["tests"] = tests

  return test_cases

test_cases = generate_test_cases()
with open('beatthespread.json', 'w') as json_file:
  json.dump(test_cases, json_file, indent = 4, sort_keys = True)

