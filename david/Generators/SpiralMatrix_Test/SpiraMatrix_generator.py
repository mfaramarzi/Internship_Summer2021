import json
import random

def SpiralMatrix(matrix, numRows, numColumns):
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

def generateMatrices():
  random.seed(500)
  
  matrices = []
  numRows, numCols = generateNumbers()
  for i in range(50):
    
    matrix_length = numRows[i] * numCols[i]
    matrices.append([random.randint(-10000,10000) for _ in range(matrix_length)])    
  
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

def generateNumbers():
  random.seed(500)
  numRows = [random.randint(3,8) for _ in range(50)]
  numCols = [random.randint(3,8) for _ in range(50)]
  return numRows, numCols


def generateCase(case, matrix, numRows, numCols):
  print("case ", case)
  new_case = {}

  strMatrix = ""
  # for i in range(len(matrix)):
  #   strMatrix += str(matrix[i]) + " "

  for i in range(numRows):
    for j in range(numCols):
      if j == numCols - 1:
        strMatrix += str(matrix[j + i * numCols])
      else:
        strMatrix += str(matrix[j + i * numCols]) + " "
    strMatrix += "\n"

  new_case["case"] = case
  new_case["input"] = "%s %s\n%s" % (numRows, numCols, strMatrix) 
 #print(numRows, numCols, matrix)
  #print(SpiralMatrix(matrix,numRows,numCols))

  result = SpiralMatrix(matrix,numRows,numCols)
  new_case["output"] = "%s" % (result)

  return new_case

def generateTestCases():

  
  matrices, numRows, numCols = generateMatrices()

  test_cases = {}
  tests = []    

  for i in range(len(matrices)):
    tests.append(generateCase(i + 1, matrices[i], numRows[i], numCols[i]))
  
  test_cases["tests"] = tests

  return test_cases

test_cases = generateTestCases()
with open('SpiralMatrix.json', 'w') as json_file:
  json.dump(test_cases, json_file, indent = 4, sort_keys = True)


