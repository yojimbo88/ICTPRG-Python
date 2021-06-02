# create function GetPassword.
def GetPassword():
    # introduction.
    print("Password criteria:\n- 1 lowercase letter.\n- 1 uppercase letter.\n- 1 number.\n- 1 symbol\n- Password is at least 7 characters long.\n- Does not contain the word 'password'")
    while True:
        try:            
            password = input("Please, enter password: ")
            char = list(password)
            #establishing parameters for password.
            symbols = ["@","_","!","#","$","%","^","&","*","(",",",")","<",">",",",",","+","-",";",":","/",]
            parameters = []
            if len(char) < 7:
                parameters.append("Password needs to be more than 7 characters.")
            if not any(char.isdigit() for char in password):
                parameters.append('Password should have at least one number.')
            if not any(char.isupper() for char in password):
                parameters.append('Password should have at least one uppercase letter.')
            if not any(char.islower() for char in password):
                parameters.append('Password should have at least one lowercase letter.')
            if password == "password":
                parameters.append("Password cannot be word 'password'.")
            if not any(char in symbols for char in password):
                parameters.append("Password needs to have at least one symbol.")
            # output of parameters not met in passwords.
            if parameters:
                raise ValueError("\n".join(parameters))
            else:
                print("Valid password.")
            return password
        except ValueError as error:
            print(error)
            

GetPassword()



# Q5

# def passwd_check():
#     print("Password criteria:\n- 1 lowercase letter.\n- 1 uppercase letter.\n- 1 number.\n- 1 symbol\n- Password is at least 7 characters long.\n- Does not contain the word 'password'")
#     while True:
#         try:
#             passwd = input('enter the password : ')
#             SpecialSym=['$','@','#']
#             return_val=True
#             if len(passwd) < 6:
#                 print('the length of password should be at least 6 char long')
#                 return_val=False
#             if len(passwd) > 8:
#                 print('the length of password should be not be greater than 8')
#                 return_val=False
#             if not any(char.isdigit() for char in passwd):
#                 print('the password should have at least one numeral')
#                 return_val=False
#             if not any(char.isupper() for char in passwd):
#                 print('the password should have at least one uppercase letter')
#                 return_val=False
#             if not any(char.islower() for char in passwd):
#                 print('the password should have at least one lowercase letter')
#                 return_val=False
#             if not any(char in SpecialSym for char in passwd):
#                 print('the password should have at least one of the symbols $@#')
#                 return_val=False
#             if return_val:
#                 print('Ok')
#             return return_val
#         except ValueError as error:
#             print(error)


# import re

# def check_splcharacter(test):
#     # Make own character set and pass 
#     # this as argument in compile method
 
#     string_check= re.compile('[@_!#$%^&*()<>?/\|}{~:]')
 
#     # Pass the string in search 
#     # method of regex object.
 
#     if(string_check.search(test) == None):
#         print("String does not contain Special Characters.") 
#     else: 
#         print("String contains Special Characters.")

# check_splcharacter("fdfsd%*")