arr = []                                # create empty list where number are going.
dups = set()

for n in arr:                           # for loop counting repeated element in the list.
    if arr.count(n) > 1:
        dups.add(n)
        dups = list(dups)

while True:                             # loop asking to input number, break if not int
    n = input("Enter a number: ")
    if n.isnumeric():
        n = int(n)
        arr.append(n)
    else:
        break

print("You entered: ", list({n for n in arr if arr.count(n) > 1}))
#Tomas Franco 101399521


# numbers = dict()
# while True:
#     n = input("Enter a number: ")
#     if n.isnumeric():
#         value = numbers.get(int(n), 0)
#         numbers[int(n)] = value + 1
#     else:
#         break
# while True:
#     k = []
#     v = k in numbers.items()
#     if v > 1:
#         print(k)