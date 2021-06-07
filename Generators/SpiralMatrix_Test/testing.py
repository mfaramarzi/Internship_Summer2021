import random
def generateMatrices():
  random.seed(500)
  
  matrices = []
  for i in range(50):
    matrix_length = random.randint(0,100)
    matrices.append([random.randint(-100,100) for _ in range(matrix_length)])
  print(matrices)
  return matrices
generateMatrices()