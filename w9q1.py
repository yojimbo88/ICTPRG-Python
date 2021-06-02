# open a read/write file named maths.txt
file = open("maths.txt", "w")

# introducing the variables
number1 = input("Number 1: ")
number2 = input("Number 2: ")

# addition of variable after converting them into integers
addition = int(number1) + int(number2)

# output of the number introduced as well as the reseult of the addition between them
file.write("Number 1 is: " + number1 + "\n")
file.write("Number 2 is: " + number2 + "\n")
file.write("The addition of number 1 and number 2 is :" + str(addition))


print(number1)
print(number2)
print(addition)