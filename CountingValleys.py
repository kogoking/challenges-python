# Counting Valleys Problem - HackerRank

s = "UDDDUDUU"

g=0 #ground level
v=0 #number of valleys
for i in s:
  if i == "D":
    g = g-1
  else:
    g = g+1
  if(g == 0 and i == 'U'):
    v=v+1;

# Printing level and amount of valleys crossed
print(g)
print(v)