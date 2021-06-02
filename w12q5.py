# Write the function between the START and END tags
# START

def IsPalindrome(word):
    # convert string into lowercase.
    word = word.lower()
    # replace space in sentence with no space.
    word = word.replace(" ", "")
    # reverse content of string.
    return word == word[::-1]

# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE
print("Test 1 Passed: " + str(IsPalindrome("GlenElg") == True))
print("Test 2 Passed: " + str(IsPalindrome("Nurses Run") == True))
print("Test 3 Passed: " + str(IsPalindrome("Nurses") == False))
print("Test 4 Passed: " + str(IsPalindrome("frank") == False))



# def IsPalindrome(word):
#     reversed_string = word[::-1]
#     status=1
#     if word == reversed_string:
#         status=0
#     return status

# def IsPalindrome(word):
    # return word != word[::-1]