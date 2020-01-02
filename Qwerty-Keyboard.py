# This code displays the letter on the right key (of the key you press while entering the string) of the keyboard in the form of string.
# Eg: 'wasd' gives output as 'esdf'.

k = "qwertyuiop[]asdfghjkl;'zxcvbnm,./"
key = list(k)

input = input("Enter string: ")
list = list(input)

n = len(key)

for i in range(0,len(list)):
  for j in range(0,n):
    if key[j]==list[i]:
      list[i]=key[j-1]

print("Decoded:  ")
for i in list:
  print(i,end="")