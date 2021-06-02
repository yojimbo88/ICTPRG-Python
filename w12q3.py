# Write the function between the START and END tags
# START

def FibonacciAdder(n):
    # establishing the position of the number and its addition.
    if n <= 1:
       return n
    else:
       return FibonacciAdder(n-1) + FibonacciAdder(n-2)

# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE
print("Test 1 Passed: " + str(FibonacciAdder(2) == 1))
print("Test 2 Passed: " + str(FibonacciAdder(5) == 7))
print("Test 3 Passed: " + str(FibonacciAdder(10) == 88))