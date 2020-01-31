# Checking if number is prime number or not
def isPrime(num):
  if num > 1:
    for i in range(2,num):
      if (num % i) == 0:
        return False
    else:
        return True
  else:
    return False

# Checking if number is smith number or not
def isSmith(num):

	a = num
	i=2
	factorList = []

	# Logic
	while(i<=a):
		if(a%i==0):
			factorList.append(i)
			a = a/i
			i = 2
		if(a%i!=0):
			i = i+1

	# Creating factor list for addition
	factorList = [str(x) for x in factorList]
	factorList = ''.join(factorList)
	factorList = list(factorList)
	factorList = list(map(int, factorList))

	# Function output
	if(sum(factorList) == sum(numList)):
		return True
	else:
		return False

# Start
numString = input("Enter number: ")
numList = list(numString)
numList = list(map(int, numList))
num = int(numString)

# Smith number is always composite number.
if(isPrime(num)):
	print("Not Smith")
else:	
	if(isSmith(num)):
		print("It's Smith")
	else:
		print("Not Smith")