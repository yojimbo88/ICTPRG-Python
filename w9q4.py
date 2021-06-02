# open write text file
file = open("factorial.txt", "w")

# variable that is a list containing numbers from 1 to 10
n = [1,2,3,4,5,6,7,8,9,10]

fact = 1

# loop that takes number from list and multiplies them as factorial
for i in range(1,n[9]+1):
    fact = fact * i
    file.write(str(fact) + "\n")
    

# import math

# list = [1,2,3,4,5,6,7,8,9,10]
# print(math.factorial(list[0]))
# print(math.factorial(list[1]))
# print(math.factorial(list[2]))
# print(math.factorial(list[3]))
# print(math.factorial(list[4]))
# print(math.factorial(list[5]))
# print(math.factorial(list[6]))
# print(math.factorial(list[7]))
# print(math.factorial(list[8]))
# print(math.factorial(list[9]))


