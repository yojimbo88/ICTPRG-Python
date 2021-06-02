arr = []                                # create empty list where number are going.

while True:                             # loop asking to input numbers into the list.
    n = input("Enter a number: ")
    
    if n.isnumeric():                   # if statement if input is not an int the break loop and prit list.
        n = int(n)
        arr.append(n)
    else:
        break
        
print("You entered: ", arr)

# Tomas Franco 101399521

# l = []
# while True:
#     i = input('Enter a number: ')
#     if not i.isnumeric():
#         break
#     l.append(int(i))
# print('You entered', l)