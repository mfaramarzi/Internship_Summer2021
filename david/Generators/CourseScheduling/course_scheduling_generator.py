import json
import random

def GetNames()->(list[str],list[str]):
  fileName = "names.csv"
  firstNames = []
  lastNames = []
  inFile = open(fileName, 'r')

  line = inFile.readline()

  for line in inFile:
    line = line.strip()
    first, last = line.split(",")
    assert(len(first) < 20 and len(last) < 20)
    firstNames.append(first)
    lastNames.append(last)

  inFile.close()

  return firstNames, lastNames


def generateCourseName()->str:

  choices = ["CSC", "CSS","MTH","CS","PHY","BIO","MUS","COM","CHM","GEO"]
  numbers = [random.randint(0,9) for _ in range(random.randint(0,5))]
  
  randIdx1 = random.randint(0,9)
 

  return choices[randIdx1] + "".join([str(num) for num in numbers])


def generateCourseNameCombo(firstNames, lastNames):
  
  random.seed()
  fname = firstNames[random.randint(0,len(firstNames)-1)]
  lname = lastNames[random.randint(0,len(lastNames)-1)]
 
  course = generateCourseName()

  return fname, lname, course


def solve(fnames, lnames, courses):
  outStr = ""
  courseMap = {}
  for c in courses:
    courseMap[c] = 0
 
  used = []

  for f, l, c in zip(fnames, lnames, courses):
    if (f,l,c) not in used:
      used.append((f,l,c))
      courseMap[c] += 1

  for course in sorted(courseMap.keys()):
    outStr += course + " " + str(courseMap[course]) + "\n"

  return outStr


def generateInput(firstNames, lastNames, maxNames, count):
  numNames = random.randint(0, maxNames)
  #numNames = 10
  fnames = []
  lnames = []
  courses = []
  
  print("input ", str(maxNames) + " " + str(count))
  
  for i in range(numNames):
    fname, lname, course = generateCourseNameCombo(firstNames, lastNames)
    fnames.append(fname)
    lnames.append(lname)
    courses.append(course)

  
  if len(fnames) >= 10:
    numFullDuplicates = random.randint(0,int(len(fnames)/5))

    for i in range(numFullDuplicates):
      idx1 = random.randint(0, len(fnames)-1)
      idx2 = random.randint(0, len(fnames)-1)
     

      fnames[idx1] = fnames[idx2]
      lnames[idx1] = lnames[idx2]
      courses[idx1] = courses[idx2]

    numCourseDuplicates = random.randint(1,int(len(fnames)/3))
    for n in range(numCourseDuplicates):
      idx1 = random.randint(0, len(fnames)-1)
      idx2 = random.randint(0, len(fnames)-1)
      courses[idx1] = courses[idx2]
  
  return fnames, lnames, courses


# Generate each individual test case
def generateCase(case, fnames, lnames, courses):

  new_case = {}
  assert(len(fnames) == len(lnames) == len(courses))
  numStudents = len(fnames)

  inStr = str(numStudents) + "\n"
  for f,l,c in zip(fnames, lnames, courses):
    inStr += f + " " + l + " " + c + "\n"  

  new_case["case"] = case
  new_case["input"] = "%s" % (inStr)

  result = solve(fnames, lnames, courses)
  new_case["output"] = "%s" % (result)

  return new_case

# Create list of all 50 test cases with case #, input, expected output
def generateTestCases():
  fnames, lnames = GetNames()

  
  
  test_cases = {}
  tests = []
  maxNames = 2
  for i in range(1,50):    
    f,l,c = generateInput(fnames, lnames, maxNames,i)
    tests.append(generateCase(i + 1, f,l,c))
    if i % 5 == 0:
      maxNames *= 2
    else:
      maxNames += 3

  test_FN = ["PINK","JOHN","JOHN","JOHN"]
  test_LN = ["TIE","DOE","DOE","DOE"]
  test_CS = ["CSC241", "CSC241", "CSS","CSS"]

  tests.insert(0, generateCase(1,test_FN,test_LN,test_CS))
  
  test_cases["tests"] = tests

  return test_cases

test_cases = generateTestCases()
with open('CourseScheduling.json', 'w') as json_file:
  json.dump(test_cases, json_file, indent = 4, sort_keys = True)

# print(generateInput())
#print("----")
#print(generateCourseNameCombo())