# variables asking users to input name a password
name = input("Enter name: ")
password = input("Enter password: ")

# writing above variables in text file as "user4:password3"
with open("user.txt", "w") as file:
    file.writelines(name + ":" + password)
    file.close()

username = "user4"
passw = "password3"

# taking "user4:password3" from text file
with open("user.txt") as file2:
    line = file2.readlines()
    # putting content of text file into a list
    newline = []    
    # loop splitting contents in list 
    for i in line:
        newline = i.split(":")
        # logic comparing correct name and password and if correct to output in text file
        if username == newline[0] and passw == newline[1]:
            with open("logins.txt", "w") as file2:
                file2.writelines("Username? : " + newline[0] + " " + "password?: " + newline[1] + " " + "Access Granted!")
    





# with open("logins.txt", "w") as file2:
#     while True:
#         if username == "user4" and password == "password3":
#             file2.write("Username? ")