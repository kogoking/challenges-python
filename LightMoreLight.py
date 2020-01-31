# number of bulbs
# i-th walk is one oscillation
# find final state
import math

zz = int(input("Enter any number: "))
while(zz!=0):
  x = math.sqrt(zz)
  if(x*x == zz):
    print("Yes")
  else:
    print("No")
  zz = int(input("Enter any number: "))



