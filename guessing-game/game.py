"""A number-guessing game."""
# Updated by Jordan Leich on 5/20/2020, email me at jordanleich@gmail.com if you want to make any python programs
# together please!

# Imports
import random
import time

# Intro code
mood = input("Hello, how are you? ")
print()
time.sleep(1)
name = input("What's your name? ")
print()
time.sleep(1)


# Core code for the guessing game
def game():
    right_number = random.randint(1, 100)
    num_guesses = 0
    guess_number = int(input("Hi " + name + ", please guess a number between 1-100: "))

    if guess_number == right_number:
        print()
        print('Congrats ' + name + ', you have guessed the correct number in ' + str(num_guesses) + " tries!")
        print()
        time.sleep(2)
        quit()

    elif guess_number < right_number:
        print()
        print("Please guess a higher number.")
        num_guesses += 1
        print()
        game()

    elif guess_number > right_number:
        print()
        print("Please guess a lower number.")
        num_guesses += 1
        print()
        game()

    elif guess_number < 0 or guess_number > 100:
        print()
        print("Only guess a number between 1 and 100 please.")
        print()
        time.sleep(2)
        game()

    elif guess_number == right_number:
        print()
        print('Congrats ' + name + ', you have guessed the correct number in ' + str(num_guesses) + " tries!")
        print()
        time.sleep(2)
        quit()

    else:
        print("Error!")
        print()
        time.sleep(5)


# Starts the guessing game code above
game()
