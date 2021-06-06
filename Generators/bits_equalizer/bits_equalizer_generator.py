import json
import random
import math

class TestWrapper:

    def __init__(self, num : int):
        self.numCases = num
        self.strList : list[StrPair]= []

class StrPair:

    def __init__(self, str1 : str, str2 : str):        
        self.str1 = str1
        self.str2 = str2

def buildStrPair(count : int):

    random.seed(count)
    
    stringLen = random.randint(1,100)

    str1 = ""
    str2 = ""
    chars = ['0','1','?']

    for i in range(stringLen):
        str1 += (chars[random.randint(0,2)])
        str2 += (chars[random.randint(0,1)])
        
    return StrPair(str1, str2)


def buildTestWrapper(count : int):
    random.seed(count)   
    currentCase = TestWrapper(random.randint(1,200))

    for i in range(currentCase.numCases):
        currentCase.strList.append(buildStrPair(count + i))

    return currentCase

        
def solve(currentTest : TestWrapper):
    outStrList : list[str] = []
    for i in range(currentTest.numCases):
        currentPair : StrPair = currentTest.strList[i]
        
        s1 = currentPair.str1
        s2 = currentPair.str2

        a = 0
        b = 0
        c = 0
        d = 0
        e = 0
        f = 0

        for j in range(len(s1)):
            if(s1[j] == '0' and s2[j] == '0'): a+=1
            if(s1[j] == '0' and s2[j] == '1'): b+=1
            if(s1[j] == '1' and s2[j] == '0'): c+=1
            if(s1[j] == '1' and s2[j] == '1'): d+=1
            if(s1[j] == '?' and s2[j] == '0'): e+=1
            if(s1[j] == '?' and s2[j] == '1'): f+=1

        ans = 0
        ans = min(b,c)
        b -= ans
        c -= ans

        if b > 0:
            ans += b + e + f
        else:
            if f < c:
                ans = -1
            else:
                ans += c
                e -= c

                ans += c
                ans += e+f

        outStrList.append("Case {}: {}\n".format(i + 1,ans))
    return outStrList




def generateCase(case,  input : TestWrapper):

    inputStr = str(input.numCases) + "\n"

    for i in range(input.numCases):
        inputStr += input.strList[i].str1 + "\n" + input.strList[i].str2 + "\n"
    inputStr.strip("\n")

    solution = solve(input)

    solStr = "".join([str(sol) for sol in solution])

    print(solStr)


    new_case = {}

    new_case["case"] = case
    new_case["input"] = "%s" % (inputStr)     
   
    new_case["output"] = solStr

    

    return new_case

def generateTestCases():

    myTestCases = []
    for i in range(50):
        myTestCases.append(buildTestWrapper(i))   

    firstTest = TestWrapper(0)   
    firstTest.strList.append(StrPair("01??00","001010"))
    firstTest.strList.append(StrPair("01","10"))
    firstTest.strList.append(StrPair("110001","000000"))
    firstTest.numCases = 3

    myTestCases[0] = firstTest

    test_cases = {}
    tests = []
    for i in range(len(myTestCases)):
        tests.append(generateCase(i + 1, myTestCases[i]))
    
    
    test_cases["tests"] = tests

    return test_cases

test_cases = generateTestCases()
with open('bits_equalizer.json', 'w') as json_file:
  json.dump(test_cases, json_file, indent = 4, sort_keys = True)

# str1, str2 = generateStrings(1)
# sp = StrPair(str1,str2)

# sp = buildStrPair(1)
# print(sp.str1)

# print("-----")

# tw = buildTestWrapper(2)
# sp1 = tw.strList[0].str1
# sp2 = tw.strList[0].str2
# print(sp1,sp2)