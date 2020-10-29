
arr = []
n= int(input("Enter a number of elements: "))
print("enter one by one")

for i in range(0,n):
    element = int(input())
    arr.append(element)

arr.sort()
arr = list(dict.fromkeys(arr))

subsetA = []
subsetB = arr

numOfElem = len(arr)
arrangements = 2**numOfElem

def combination(arr):
    rolproduct = 1
    for i in arr:
        rolproduct = rolproduct * i
    return rolproduct

print("You can have a total of " + str(combination(arr)) + " arrangements of these numbers")

maxSum = 0

print("the number of integers entered is " + str(numOfElem))

def splitArray(arr,subsetA,subsetB):
    A = len(subsetA)
    B = len(subsetB)
    lenOfArr = len(arr) 

    for i in arr:   
        if lenOfArr > A:
            elem_1 = arr.pop()
            elem_2 = arr.pop()
            subsetA.insert(0,elem_1)
            subsetA.insert(0,elem_2)
            subsetB = arr
        return subsetB, subsetA 

splitArray(arr,subsetA,subsetB)

print("subset A is " + str(subsetA) + " and subset B is " + str(subsetB)) 

def maxSum (subsetA,subsetB):
    sumB = sum(subsetB) 
    sumA = sum(subsetA)
    while sumA < sumB: 
        subsetA.insert(0,subsetB.pop())
    else:
        max = sumA
    return max

print("the max sum of the minimal of 2 elements of subset A is " + str(maxSum(subsetA,subsetB)))



##
