# FIRST INPUT LINE
firstInputLine = input("Enter max slices and amount of pizza separated by space: ")
tempArray = firstInputLine.split()
# STRING LIST TO INT LIST
tempArray = list(map(int, tempArray))


# INITIALIZING
maxSlices = tempArray[0]
pizzaAmount = tempArray[1]


# SECOND INPUT LINE
secondInputLine = input("Enter number of slices in pizza separated by space: ")
sliceList = secondInputLine.split()
# STRING LIST TO INT LIST
sliceList = list(map(int, sliceList))
sliceListCopy = list(map(int, sliceList))


# OUTPUT VALUE LIST (ADDED 0 AT DECLARATION)
outputValueList = [0]
outputIndexList = []


# LOGIC
for x in range(pizzaAmount):
  if(max(sliceList) <= maxSlices - sum(outputValueList)):
    outputValueList.append(max(sliceList))
    sliceList.remove(max(sliceList))
  else:
    sliceList.remove(max(sliceList))

outputValueList.pop(0)

for i in outputValueList:
  outputIndexList.append(sliceListCopy.index(i))

outputIndexList.sort()
outputIndexString = " ".join(map(str, outputIndexList)) # SEPARATING INT VALUES BY SPACE


# OUTPUT IN CONSOLE 
print(len(outputIndexList))
print(outputIndexString)