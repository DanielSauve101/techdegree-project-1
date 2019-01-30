"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random

"""Psuedo-code Hints

    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".

    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.

    ( You can add more features/enhancements if you'd like to. )
    """
# write your code inside this function.
solution = random.randint(1, 10)

guesses = []

print("""
-----------------------------
Welcome to the Guessing Game!
-----------------------------
""")

# def start_game():
player_name = input("Please enter your name:  ")

print("""
Good luck {}!
Remember to have fun!!
""".format(player_name))

start = input("Are you ready to begin? (Y)es or (N)o:  ")


while start.lower() == "y":
    guess = int(input("What number would you like to try (1-10):  "))
    if guess > solution:
        guesses.append(guess)
        print("The magic number is lower then {}.".format(guess))
        continue
    elif guess < solution:
        guesses.append(guess)
        print("The magic number is higher then {}.".format(guess))
        continue
    elif guess == solution:
        guesses.append(guess)
        if len(guesses) == 1:
            print("Wow!! Lucky guess. You have found the magic number on your first try!!!")
            break
        else:
            print("Good game. You have found the magic number in {} tries!!!".format(len(guesses)))
            break
print("Have a good day {} and come back and play anytime.".format(player_name))

# if __name__ == '__main__':
#     # Kick off the program by calling the start_game function.
#     start_game()
