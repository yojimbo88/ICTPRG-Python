number = input("Enter a large number: ")   # # user input variable for name.

lst = [int(x) for x in str(number)]        # variable in which a loop will be a list with the input str elements 
                                           # it will convert the str into integers
print("Sum of the digits: ", end="")
print(*lst, sep=" + ", end="")
print(" = " + str(sum(lst)))               # statement broken for better output with the total some of elements.

# Tomas Franco 101399521