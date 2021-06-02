name = input("Enter your name: ")           # user input variable for name.

name2 = name.split(" ")                     # split string into a list split by " " (space).
initials = ""

for i in range(len(name2)):                 # loop that takes the first letter of each part of the name.
    name = name2[i]
    initials = initials + name[0].upper()   # this the first letter of each word and makes it upper case.

print("Initials: ", initials)

# Tomas Franco 101399521