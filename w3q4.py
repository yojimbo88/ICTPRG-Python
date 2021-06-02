name = input("Enter name: ")                                    # input of a name as a variable.
password = input("Enter password: ")                            # input of a password as a variable.

if name == "bob" and password == "password1234":                # if statement of name bob and password match the grant access.
    print("Access Granted!")
elif name == "fred" and password == "happyPass122":             # if statement of name fred and password match the grant access.
    print("Access Granted!")
elif name == "lock" and password == "passwithlock44":           # if statement of name lock and password match the grant access.
    print("Access Granted!")
else:                                                           # if not any of the names above then deny access.
    print("Access Denied!")

# Tomas Franco 101399521