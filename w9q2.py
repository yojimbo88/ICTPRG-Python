# open a read/write file named people.txt
file = open("people.txt", "w")

# while loop asking user to input name, will end loop if nothing is entered
while True:
    name = input("Enter name: ")
    if name == "":
        break
    file.write(name + "\n")