import json
import random
import math

#solution translated from https://github.com/mpfeifer1/Kattis/blob/master/alldifferentdirections.cpp

class Vector2f:  
    def __init__(self, x : float, y: float):
        self.x = x
        self.y = y

def dist(p1 : Vector2f, p2 : Vector2f) -> float:
    return math.sqrt(math.pow(p1.x-p2.x,2) + math.pow(p1.y-p2.y,2))

def dist1(x1 :float, y1: float, x2 : float, y2: float) -> float:
    return math.sqrt(math.pow(x1-x2,2) + math.pow(y1 - y2, 2))

# Class holds each inidividual instruction a person can give ex: walk 5
class Instruction:
    kind : str = ""
    value : float = 0.0
    def __init__(self, instruction: str, val: float):
        self.kind = instruction
        self.value  = val

# Contains all of the instructions given by one person - start point and a list of instructions
class Directions:
    def __init__(self):
        self.instructionList : list[Instruction] = []
        self.startPoint : Vector2f = Vector2f(0.0,0.0)

# Calulcates x movement
def moveX(dist: float, angle: float) -> float:
    return dist * math.cos(angle * math.pi/180)

# Calulcates y movement
def moveY(dist: float, angle: float) -> float:
    return dist * math.sin(angle * math.pi/180)
    
# Function to solve question and provide output
def solve(numPeople : int, directions : list[Directions]) -> (float,float,float):

    destinationList : list[Vector2f] = []

    # Loop through all instructions from people, calc destination per person and append to list
    for i in range(numPeople):
        angle :float = 0.0
       
        tempDir: Directions = directions[i]
        currentPos: Vector2f = Vector2f(0,0)
        currentPos.x = tempDir.startPoint.x
        currentPos.y = tempDir.startPoint.y
       
        for instruction in tempDir.instructionList:
            tempInstr : Instruction = instruction
            
            if tempInstr.kind == "start":
                angle = tempInstr.value
            elif tempInstr.kind == "walk":
                currentPos.x += tempInstr.value * math.cos(angle * math.pi/180)
                currentPos.y += tempInstr.value * math.sin(angle * math.pi/180)
                # currentPos.x += moveX(tempInstr.value, angle)
                # currentPos.y += moveY(tempInstr.value, angle)
            elif tempInstr.kind == "turn":
                angle += tempInstr.value           

        destinationList.append(currentPos)

    # Calculate average destination
    averageDest : Vector2f = Vector2f(0.0, 0.0)
    for destination in destinationList:       
        averageDest.x += destination.x
        averageDest.y += destination.y
    averageDest.x /= len(destinationList)
    averageDest.y /= len(destinationList)

    maxDist : float = 0.0
    for dest in destinationList:     
        tempDist = dist1(averageDest.x, averageDest.y, dest.x,dest.y)      

        if(tempDist > maxDist):
            maxDist = tempDist
      
    return averageDest.x, averageDest.y, maxDist

def generateRandomFloat(count: int) -> float:
    random.seed(count)
    return round(random.uniform(-1000,1000),4)

def generateInstructionChoice(count : int) -> str:
    instructionOptions : list[str] = ["turn", "walk"]
    instructionChoice : str = instructionOptions[random.randint(0,1)]
    return instructionChoice

def generateNumInstructionsPerPerson(count : int) -> int:
    random.seed(count)
    return random.randint(1,25)

# generates directions given by one person
def generateDirections(count : int) -> Directions: 

    directions : Directions = Directions()    
    directions.startPoint = generateRandomPoint(count)
    directions.instructionList.append(Instruction("start", generateRandomFloat(count)))

    for i in range(generateNumInstructionsPerPerson(count)):
        
        directions.instructionList.append(Instruction(generateInstructionChoice(count + i),generateRandomFloat(count + i)))   

    return directions

def generateRandomPoint(count : int) -> Vector2f:
    random.seed(count)
    randx = round(random.uniform(-1000,1000),4)
    randy = round(random.uniform(-1000,1000),4)
    return Vector2f(randx,randy)

# Each case contains up to 100 mini cases - this generates one such mini case
def generatePartialCase(count: int) -> list[Directions]:
    numPeoplePerCase : int = random.randint(1,20)

    directions : list[Directions] = []

    for i in range(numPeoplePerCase):            
       directions.append(generateDirections(i + count))

    return directions

# Generates one full case - aggregate of mini-cases
def generateFullCase(count : int):
    random.seed(count)
    numCases : int = random.randint(1,100)

    allCases : list[list[Directions]] = []

    for i in range(numCases):
        allCases.append(generatePartialCase(count))

    return allCases


def generateCase(case : int, input1 : list[list[Directions]]):

    new_case = {}
   
    inputStr = ""  
    for input in input1:
        inputStr += str(len(input)) + "\n"
        for dirs in input:
            a : Directions = dirs
            inputStr += str(a.startPoint.x) + ' ' +  str(a.startPoint.y) + ' '
            for i in dirs.instructionList:
                inputStr += i.kind + ' ' + str(i.value) + ' '
            inputStr = inputStr.strip()
            inputStr += "\n"
        inputStr += str(0) 

    new_case["case"] = case
    new_case["input"] = "%s" % (inputStr) 
    solStr = ""#"{:.4f} {:.4f} {:.4f}".format(x,y,dist)

    for input in input1:
        x,y,dist = solve(len(input),input)  
        solStr += "{:.4f} {:.4f} {:.4f}\n".format(x,y,dist)
    solStr = solStr.strip("\n")
   
    new_case["output"] = solStr

    return new_case

# Hard-coded case from Kattis
def generateBaseCase1() -> list[Directions]:

    numPeople : int = 3

    startingPoint : Vector2f = Vector2f(87.342, 34.30)

    allDirections :list[Directions] = []

    directions : Directions = Directions()
    directions.startPoint = startingPoint
    directions.instructionList.append(Instruction("start",0))
    directions.instructionList.append(Instruction("walk",10.0))

    allDirections.append(directions)

    directions1 : Directions = Directions()
    directions1.startPoint = Vector2f(2.6762, 75.2811)
    directions1.instructionList.append(Instruction("start",-45.0))
    directions1.instructionList.append(Instruction("walk",40.0))
    directions1.instructionList.append(Instruction("turn",40.0))
    directions1.instructionList.append(Instruction("walk",60))

    allDirections.append(directions1)

    directions2 : Directions = Directions()
    directions2.startPoint = Vector2f(58.518, 93.508)
    directions2.instructionList.append(Instruction("start",270))
    directions2.instructionList.append(Instruction("walk",50))
    directions2.instructionList.append(Instruction("turn",90))
    directions2.instructionList.append(Instruction("walk",40))
    directions2.instructionList.append(Instruction("turn",13))
    directions2.instructionList.append(Instruction("walk",5))

    allDirections.append(directions2)  
    return allDirections

# Hard-coded case from Kattis
def generateBaseCase2():
    directions3 = Directions()
    directions3.startPoint = Vector2f(30.0,40.0)
    directions3.instructionList.append(Instruction("start",90))
    directions3.instructionList.append(Instruction("walk",5))

    allDirections2 : list[Directions] = []
    allDirections2.append(directions3)

    directions4 = Directions()
    directions4.startPoint = Vector2f(40,50)
    directions4.instructionList.append(Instruction("start",180))
    directions4.instructionList.append(Instruction("walk",10))
    directions4.instructionList.append(Instruction("turn",90))
    directions4.instructionList.append(Instruction("walk",5))
    allDirections2.append(directions4)

    return allDirections2

# Hard-coded case from Kattis
def generateBaseCase() -> list[list[Directions]]:
    case : list[list[Directions]] = []

    case.append(generateBaseCase1())
    case.append(generateBaseCase2())

    return case

def generateTestCases():

    myTestCases = []
    for i in range(50):
        myTestCases.append(generateFullCase(i))   
  
    myTestCases[0] = generateBaseCase()

    test = generateBaseCase()   

    test_cases = {}
    tests = []
    for i in range(50):
        tests.append(generateCase(i + 1, myTestCases[i]))

    test_cases["tests"] = tests

    return test_cases

test_cases = generateTestCases()
with open('AllDifferentDirections.json', 'w') as json_file:
  json.dump(test_cases, json_file, indent = 4, sort_keys = True)
