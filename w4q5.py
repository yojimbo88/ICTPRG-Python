# print("Enter some numbers (Press x to stop): ")     # statement asking user to enter number

# total = 0

# while True:                                         # loop that will add all the entered numbers
#     number = input("")                              
#     if number == "x" :                              # loop only broken when entering x
#         break
#     total = total + int(number)
# print("Total: ",total)

# Tomas Franco 101399521

# --------------------------------------------------------------------------------------------------------------
sum = 0
num = input("Enter some numbers (Press x to stop):\n")

while num != "x":
    sum = sum + int(num)
    num = input()

print("Total: ",sum)

# --------------------------------------------------------------------------------------------------------------

# print("Enter some number (Press x to stop): ")

# sum = 0

# while True:
#     x = input("")
#     while x == "x":
#         print("Total: ",sum)
#         break
#     while int(x) >= 0:
#         sum += int(x)
#         break

# ----------------------------------------------------------------------------------------------------------------
# total = 0

# print("Enter some number (Press x to stop): ")

# while True:
#         number = input("")
#         if number == "x":
#             break
#         try:
#             total = total + int(number)
#         except:
#             continue

# print('Total:',total)
