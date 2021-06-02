# introduction/instructions.
print("Input Details")

# loop requesting user to input details, loop will break if user leaves it blank in any instance.
while True:
    first_name = input("First name: ")
    if first_name == "":
        print("First name left blank.")
        break
    last_name = input("Last name: ")
    if last_name == "":
        print("Last name left blank.")
        break
    age = input("Age: ")
    if age == "":
        print("Age left blank.")
        break

# variable introducing ID number as a list of string.    
    student_id = list(str(101399521))
# variable introducing the 3rd to last digit of ID number.    
    id_3rd_last = int(student_id[-3])
# variable below offsetting the user's age by the 3rd to last digit of ID number.
    year = 2021 - int(age)
    year_output = year - id_3rd_last

# variables converting the user's input into a list.    
    first_letter = list(first_name)
    first_letter2 = list(last_name)

# variable that will determine the user's domain as a string.
    email = "@Huawow.io"

# output the combination of first letter of name and surname as well as password (name and upper case first letter of surname) in the same line separated by "|".
    print(first_letter[0].lower() + last_name.lower() + email, end="|")
    print(first_name.lower() + first_letter2[0].upper() + "_" + str(year_output))

# Tomas Franco 101399521.