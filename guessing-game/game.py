"""A number-guessing game."""

from random import randrange

# Put your code here
print("Hi how are you? ")
users_name = input("What's your name? ")
guess_number = int(input("Hi " + users_name + " please guess a number between 1-100: "))
right_number = 25

num_guesses = 0 
while guess_number != right_number: 
    try:
        guess = int(guess_number)
    except ValueError:
        print(f'"{guess_number}" is not a valid number, try again.')
        continue

    if guess_number < 0 or guess_number > 100:
        print("Please guess a number between 1 and 100")
    
    guess_number = int(input("Hi " + users_name + " please guess a number: "))

    if guess_number < right_number:
        print("Please guess a higher number.")
        

    elif guess_number >  right_number:
        print("Please guess a lower number.")

    else:
        print("You guessed the right number in " + str(num_guesses) + " tries!")
        break
    
    num_guesses += 1
