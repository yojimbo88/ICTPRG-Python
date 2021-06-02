x = int(input("Enter a number: "))          # variable input integer number

while x not in range(50,71):                # while loop will only be broken if input integer is between 50 and 70 
    print("Not within range.")              # if loop not broken then it will keep saying "Not within range"
    x = int(input("Enter a number: "))

print("Within range.")

# Tomas Franco 101399521