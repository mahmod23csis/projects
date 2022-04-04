from collections import Counter

myDict = {"111": [90, 80, 85], "222": [70, 79, 65], "333": [83, 85, 89]}
newList = []
for key in myDict:
    for item in myDict[key]:
        newList.append(item)
maxList = []
for num in range(3):
    maxNewList = max(newList)
    index = newList.index(maxNewList)
    newList.pop(index)
    maxList.append(maxNewList)
print(maxList)
###
myDict = {'Math':81, 'Physics':83, 'Chemistry':87}
newList = []
for key in myDict:
    newList.append((key, myDict[key]))
numStuList = []
for key in myDict:
    numStuList.append(myDict[key])
numStuList.sort(reverse=True)
finalList = []
for num in numStuList:
    for major in newList:
        if num == major[1]:
            finalList.append(major)
print(finalList)
###
d1 = {'a': 100, 'b': 200, 'c':300, 'e':90}
d2 = {'a': 30, 'b': 20, 'd':40, 'c':10}

d3 = Counter(d1) + Counter(d2)
print(d3)
