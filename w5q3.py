values = [89,456,4,55,232,2,54,78,65,45,12,459,35616,45,78]

total = 0
average = 0
i = 0

while i < len(values):                  # while loop that will sum and average all items within above list.
    total += values[i]                  # each item will be reached by the index (letter i).
    average = total // len(values)
    i += 1                              # increase the variable i by one for every time the loop runs.

maximum = max(values)

print("Sum Total: ", total)                 # ouput results of avera and total sum and max number.
print("Average Total: ",(average))
print("Maximum Number in list: ", maximum)

# Tomas Franco 101399521