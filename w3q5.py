grade_num = input("What was you grade: ")       # input variable determining grade.
grade_num = int(grade_num)                      # convert said variable into an integer.

if grade_num in range(90,101):                  # if statements determining the range of the grade depending on the number
    grade = '"High Distinction"'
elif grade_num in range(80,90):
    grade = '"Distinction"'
elif grade_num in range(70,80):
    grade = '"Credit"'
elif grade_num in range(50,70):
    grade = '"Pass"'

print("You will receive a ", f"{grade}")        # output of the grade depending on the number.
# Tomas Franco 101399521