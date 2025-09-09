#CHALLENGE 2
#FIND THE CHARACTER AT A SPECIFIC INDEX


myString = "Python" # P y t h o n
i = 6              # 0 1 2 3 4 5

if len(myString) == 0:
     print("String is empty.")
elif i< len(myString):
     print(myString[i])
else:
     print("Out of range.")