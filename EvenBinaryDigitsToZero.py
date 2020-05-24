binaryList = list("{0:b}".format(int(input("Enter number: "))))

i=0
while(i<len(binaryList)):
  binaryList[i]=0
  i=i+2

result = ''.join([str(x) for x in binaryList])
print(result)
