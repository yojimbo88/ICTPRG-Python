birth_year = input("What is you year of birth?\n")   # input of the year of birth as a variable.
birth_year = int(birth_year)                         # setting the year of birth variable as an integer.
age = 2021 - birth_year                              # age variable as the subtraction of the current year and year of birth.

if age >= 18:                                        # if statement determining if person is 18 years or older then he/she can drink.
    print("You are: ", f"{age} years old.")   
    print("You can come in and have a drink.")
elif age < 18:                                       # statement if person is not 18 or older, then he/she cannot come in.
    print("You are: ", f"{age} years old.")
    print("Go away. Child.")

# Tomas Franco 101399521