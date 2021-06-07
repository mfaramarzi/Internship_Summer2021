import json
import random
import math



class Vector2D:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def length(self):
    return math.sqrt(self.x*self.x + self.y * self.y)

  def dotProduct(self,other : 'Vector2D'):
    dot = self.x*other.x + self.y* other.y 
    return dot    

  def normalize(self):
    norm_vec = Vector2D(self.x/self.length(),self.y/self.length())
    return norm_vec
    



def generateNumbers():

  random.seed(500)

  list1 = [Vector2D(random.randint(-50000, 50000),random.randint(-50000, 50000)) for _ in range(50)]
  list2 = [Vector2D(random.randint(-50000, 50000),random.randint(-50000, 50000)) for _ in range(50)]  

  list1[0] = Vector2D(0,1)
  list2[0] = Vector2D(1,0)
  
  return list1,list2

def generateCase(case, v1 : Vector2D, v2 : Vector2D):

  new_case = {}

  new_case["case"] = case
  new_case["input"] = "%s %s %s %s" % (v1.x, v1.y, v2.x, v2.y)

  length1 = v1.length()
  length2 = v2.length()

  dotProduct = v1.normalize().dotProduct(v2.normalize())
  angle = ""
  if dotProduct == 0:
    angle = "Perpendicular"
  elif dotProduct > 0:
    angle = "Acute"
  else:
    angle = "Obtuse"  

  new_case["output"] = "Length of v1: {:.4f}\nLength of v2: {:.4f}\nTheir normalized dot product is {:.4f} and they are {}".format(v1.length(), v2.length(), dotProduct, angle)

  return new_case

def generateTestCases():

  list1, list2 = generateNumbers()

  test_cases = {}
  tests = []
  for i in range(len(list1)):
    tests.append(generateCase(i + 1, list1[i], list2[i]))
  
  test_cases["tests"] = tests

  return test_cases

test_cases = generateTestCases()
with open('Vector2D.json', 'w') as json_file:
  json.dump(test_cases, json_file, indent = 4, sort_keys = True)

