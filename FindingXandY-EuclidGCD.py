import math

a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))

gcd = math.gcd(a,b)
#print(gcd)

i=0
j=0
z=0

while(max(a,b) * i != gcd + min(a,b)*j):
  if(z%2==0):
    i+=1
  else:
    j+=1
  z=z+1
  
if(max(a,b)*i == gcd + min(a,b)*j):
  x = j
  y = i;

if x > 0:
  x = -x;

print("x:",x,"y:",y,"gcd:",gcd)