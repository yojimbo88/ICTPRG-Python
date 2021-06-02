# create function GetEmailAddress.
def GetEmailAddress():
    while True:
        try:
            # ask user to input email address.
            email_address = input("Enter your email address: ")
            # split input in a list with 2 items from "@" symbol.
            email = email_address.split("@")
            # loop establishing parameter of a valid email address.
            for x in email:
                if len(x) > 32 or len(x) < 2:
                    raise ValueError("Length of email needs to be between 2 and 32.")
                if "@" not in email_address:
                    raise ValueError("Not a valid email address. Try again.")
            if "." in email[1]:
                print("This is a valid email.")
            # if parameters not show result and ask user to enter again.
            else:
                raise ValueError("Not a valid email address. Try again.")
            return email_address
        except ValueError as error:
            print(error)

