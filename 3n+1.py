# WORKING CODE FOR 3N+1 CHALLENGE.

z = True
i = int(input("Enter value of i: "))
j = int(input("Enter value of j: "))
if(i>j):
  i,j=j,i

cycleList = []
maxList = []

n = i
counter = i

# Logic

while(counter <= j):
  n = counter
  z = True
  while(z):
    if(n==1):
      print("Terminated")
      z = False
    elif(n%2==0):
      n=n/2
      cycleList.append(n)
    else:
      n=n*3+1
      cycleList.append(n)
  maxList.append((len(cycleList)))
  cycleList = []
  counter = counter + 1

# Printing

print("--Cycle-List---")
print(cycleList)
print("---Max-List---")
print(maxList)
print("***ANSWER***")
print(i)
print(j)
print(max(maxList)+1)