# create function GetIpAddress.
def GetIpAddress():
    # establish loop asking user to enter IP address.
    while True:
        try:
            ip_address = input("Enter your IP address: ")
            # split input into a list by ".".
            if "." in ip_address:
                test = ip_address.split(".")
            else:
                raise ValueError("You need a '.' to separate you IP address.")
            # establish parameters for a correct IP address.
            if len(test) != 4:
                raise ValueError("Invalid IP address, incorrect number of numbers.")
            if test[0] == "0":
                raise ValueError("0 is not usable as a first digit.")
            for x in test:
                x = int(x)
                if x > 255 or x < 0:
                    raise ValueError("Not a valip IP address, number is too large.")
            # close loop if correct IP address was entered and output result.
            print("This is a correct IP address.")
            return ip_address
        except ValueError as error:
            print(error)


