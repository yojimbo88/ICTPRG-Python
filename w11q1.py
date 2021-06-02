# create function inputNumber.
def inputNumber():
    # establish loop.
    while True:
        try:
            # ask user to input number.
            number = int(input("Enter number: "))
            print(number)
            # interrupt loop when a number is not entered and output result. 
            break
        except:
            print("That's not a number!")


# flag = False

# while not flag:
#     number = input("Enter number: ")
#     if number.isdigit():
#         print(number)
#         flag = True
#     else:
#         print("That's not a number!")