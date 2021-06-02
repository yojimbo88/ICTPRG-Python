# Write the function between the START and END tags
# START

def SortWordsAlphabetically(sentence):
    # breakdown the string into a list of words  
    words = sentence.split("-")  
    # sort the list  
    words.sort()
    # join words in the list with "-"
    new_sentence = "-".join(words)
    # display the sorted words  
    return new_sentence.lower()

# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE
print("Test 1 Passed: " + str(SortWordsAlphabetically("Bob-does-not-like-frank") == 'bob-does-frank-like-not'))
print("Test 2 Passed: " + str(SortWordsAlphabetically("why-am-i-doing-this-this-is-terrible") == "am-doing-i-is-terrible-this-this-why"))
print("Test 3 Passed: " + str(SortWordsAlphabetically("frank-kill-zoe-did") == "did-frank-kill-zoe"))