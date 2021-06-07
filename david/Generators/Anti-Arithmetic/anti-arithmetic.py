

# def getInput():
#     vList = []
#     posList = []
#     while(True):
#         tempList = input().strip()
#         if len(tempList) == 1 and int(tempList) == 0:
#              break
#         else:           
#             tempList = tempList.replace(" ","")
           
#             #vList.append([int(i) for i in tempList])
#             for i 
            
#     return vList

# def antiArithmetic(progression):
#     difList = []
#     for i in range(len(progression)):
#         for j in range(i+1,len(progression)):
#             difList.append(progression[i] - [progression[j]])

#     for i in range(len(difList)):
#         for j in range(i + 1, len(difList)):



#     return True


    

def solve(n, v, pos):
    for i in range(len(v)):
        pos[v[i]] = i

    for s in range(n):
        for d in range(-n,n+1):
            if (s+d+d >= 0 and s + d + d < n):
                if (pos[s] < pos[s+d] and pos[s+d] < pos[s+d+d]):
                   
                    return "no"

    
    return "yes"


def main():    

    while True:  

        n = input()
        if(len(n) == 1 and int(n) == 0):
            break
        num = int(n[0])
        n = n.replace(" ", "")
        vList = n[2::]
        posList = [-1] * num

        print(solve(num, [int(i) for i in vList], posList))

    

main()
