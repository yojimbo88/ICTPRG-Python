# create function GetWordsFromUser with arguments.
def GetWordsFromUser(min,max):
    while True:
        try:
            # asking user to establish minimum and maximum number of words.
            min = int(input("Enter minimum number: "))
            max = int(input("Enter maximum number: "))
            # parameter establishing that min and max number are valid.
            if min >= max:
                raise ValueError("Minimum number is equal or higher than maximum number. Enter numbers again.")
            words = input("Enter a sentence between " + str(min) + " and " + str(max) + ":\n")
            # converting input into lower case characters.
            words = words.lower()
            example = words.split()
            # parameter establishing that the right number of words is entered.
            if len(example) < min or len(example) > max:
                raise ValueError("Enter correct number of words.")
            else:
                print("You followed the instructions.")
            # output of results.
            print("Words entered: ")
            print(*example, sep="\n")
            return words
        except ValueError as error:
            print(error)

