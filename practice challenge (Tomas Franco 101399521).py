# import the random library into code.
import random

# create a number that will be randomized.
rand_numb = random.randint(0,25)

# create variables for the number of guesses and log the guesses in a list.
numb_attempts = 7
log = []
guesses = 0

# Output welcome and introduction to the game.
print("Hey there! Let's play a little guessing game...\nGuess the number between 0 and 25: ")

# Loop allowing user to enter guess until turns run out.
while numb_attempts > 0:
    # Substract from the turn counter.
    numb_attempts -= 1
    # Add to the guess counter.
    guesses += 1
    # Prompt user to enter guess number.
    guess = int(input("Enter guess: "))
    # Add to the guess.
    log.append(guess)
    # Logic to check if number is the same, less or greater that the random number. Output appropiate response.
    if guess == rand_numb:
        # Logic in case user wins in the very first attempt or more than one attempt to output message accordingly.  
        if guesses == 1:
            print("Damn. You win!\nThe number was indeed", rand_numb, "\nYou guessed in", guesses, "guess.")
        elif guesses > 1:
            print("Damn. You win!\nThe number was indeed", rand_numb, "\nYou guessed in", guesses, "guesses.")
        break
    elif guess < rand_numb:
        print("No, it's greater than that.")
    elif guess > rand_numb:
        print("No, it's less than that.")
    print("You have", numb_attempts, "guesses left!")
    # Logic reminding the user about the rule of the game.
    if guess < 0 or guess > 25:
        print("Remember. Number must be between 0 and 25.")
    # Check if user lost the game by reaching number of guesses.
    if numb_attempts == 0:
        print("YOU LOSE!")
        print("The number was", rand_numb)

# Output guess log.    
print("Your guess log was:\n", log)

# Tomas Franco 101399521