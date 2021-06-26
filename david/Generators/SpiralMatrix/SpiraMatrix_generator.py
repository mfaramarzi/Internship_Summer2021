import json
import random

def solveSpiralMatrix(matrix, numRows, numColumns):
    outString = ""
    index = 0
    topRow = 0 
    botRow = numRows -1
    leftCol = 0
    rightCol = numColumns-1    
    n = 0

    if(numRows == 0 or numColumns == 0):
        return ""    

    while True:         
      for col in range(leftCol, rightCol + 1):            
          num = matrix[col + topRow * numColumns]          
          
          outString += str(num)           
          n+=1
          if n == numRows * numColumns:               
              return outString
          outString+=(',')
          outString+=(' ')            
      topRow += 1

      # -------------^^^------------------------------

      for row in range(topRow, botRow + 1):
          num = matrix[rightCol + row * numColumns]          
          outString+=(str(num))
  
          n+=1
          if n == numRows * numColumns:                
              return outString
          outString+=(',')
          outString+=(' ')
    
      rightCol -= 1

      # -------------^^^------------------------------

      for col in range(rightCol, leftCol - 1,-1):            

          num = matrix[col + botRow * numColumns]           
          outString += str(num)
          
          n+=1
          if n == numRows * numColumns:                
              return outString
          outString+=(',')
          outString+=(' ')
    
      botRow -= 1

      # ------------^^^-------------------------------


      # bot to top
      for row in range(botRow, topRow - 1,-1):            

          num = matrix[leftCol + row * numColumns]           
          outString += str(num)
          n+=1
          if n == numRows * numColumns:
              
              return outString
          outString+=(',')
          outString+=(' ')
    
      leftCol += 1
    
    return outString

# Generates all 50 test cases for matrices, rows, and columns
def generateMatrices() -> (list[list[int]], list[int], list[int]):
  random.seed(500)
  
  # List of all matrices - each matrix is stored as 1d array 
  matrices : list[list[int]]= []
  # Generate number of rows and columns
  numRows, numCols = generateRowColumnLists()

  # Create all 50 test cases
  for i in range(50):
    matrixLength : int = numRows[i] * numCols[i]
    matrices.append([random.randint(-10000,10000) for _ in range(matrixLength)])
  
  numRows[0] = 0
  numCols[0] = 0
  matrices[0] = []

  numRows[1] = 1
  numCols[1] = 1
  matrices[1] = [1]

  numRows[2] = 3
  numCols[2] = 3
  matrices[2] = [0,1,2,3,4,5,6,7,8]

  numCols[3] = 6
  numRows[3] = 1  
  matrices[3] = [2,4,6,1,3,-5]
  
  return matrices, numRows, numCols  
  

# Returns list of rows and columns for all test cases
def generateRowColumnLists() -> (list[int],list[int]):
  random.seed(500)
  numRows = [random.randint(3,8) for _ in range(50)]
  numCols = [random.randint(3,8) for _ in range(50)]
  return numRows, numCols

# Generates each individual test case
def generateCase(case : int, matrix : list[int], numRows : int, numCols : int):
  new_case = {}
  strMatrix = "" 

  # Iterate through matrix and store it in string form
  for i in range(numRows):
    for j in range(numCols):       
        strMatrix += str(matrix[j + i * numCols]) + " "
    strMatrix = strMatrix.strip()
    strMatrix += "\n"

  new_case["case"] = case
  # Format input string
  new_case["input"] = "%s %s\n%s" % (numRows, numCols, strMatrix) 

  # Get Solution
  result = solveSpiralMatrix(matrix,numRows,numCols)

  # Format output string
  new_case["output"] = "%s" % (result)

  return new_case

# Generate data for json file
def generateTestCases():  
  matrices, numRows, numCols = generateMatrices()
  test_cases = {}
  tests = []    

  # Loop through matrices and produce input/output for each test case
  for i in range(len(matrices)):
    tests.append(generateCase(i + 1, matrices[i], numRows[i], numCols[i]))
  
  test_cases["tests"] = tests

  return test_cases

test_cases = generateTestCases()
with open('SpiralMatrix.json', 'w') as json_file:
  json.dump(test_cases, json_file, indent = 4, sort_keys = True)


