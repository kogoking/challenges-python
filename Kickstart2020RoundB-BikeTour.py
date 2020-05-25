# input amount of integers
amount = int(input("Enter amount of numbers: "))
list = []

# take n amount of integers
for i in range(0,amount):
  list.append(int(input("Enter number: ")))

# required variables
counter = 0
low = 0
high = amount-1
max = 0

# logic
i = 1
while(i<high):
  if(list[i]>=max and list[i]>list[low] and list[i]>list[high] and list[i]>list[i+1] and list[i]>list[i-1]):
    max = list[i]
    counter+=1
  i+=1

print("Peaks:",counter)
## print("Peak Number:",max)
