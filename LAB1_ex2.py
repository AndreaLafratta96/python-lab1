#Acquire string from stdin
string=input("Enter a string: ")

#Save string length in a variable
length = string.__len__()

#Check for string length
if length < 2:
    output = " "
else:
    output = string[0] + string[1] + string[length-2] + string[length-1]

print(output)