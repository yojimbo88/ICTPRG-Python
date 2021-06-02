date = input("Enter date in dd/mm/yyy: ")   # input valuable for date.

separation = date.split("/")                # split above variable by / character and convert into list.

time = ("Day:-Month:-Year:")             # valuable stating day month and year.

separation2 = time.split("-")               # split above variable by - character and convert into list.

print(separation2[0],separation[0])         # output each list item of the list according its value.
print(separation2[1],separation[1])
print(separation2[2],separation[2])

# Tomas Franco 101399521

# date = input("Enter date in dd/mm/yyy: ")

# separation = date.split("/")

# time = ("Day: -Month: -Year: ")

# separation2 = time.split("-")

# print("Day: ",separation[0])
# print("Month: ",separation[1])
# print("Year: ",separation[2])


