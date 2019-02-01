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
solution = []
guesses = []
best_score = []


def play_game_option(play_game):
    if play_game.lower() == "y":
        print("\n Good luck! \n")
        start_game()
    elif play_game.lower() == "n":
        print("Maybe next time")
    else:
        print("You must use (Y) for Yes or (N) for No")
        play_game = input("Would you like to play the game? (Y)es or (N)o: ")
        play_game_option(play_game)


def add_to_guesses(guess):
    guesses.append(guess)


def clear_game():
    best_score.append(len(guesses))
    best_score.sort(reverse=True)
    guesses.clear()
    solution.clear()


def end_game():
    if best_score[-1] == 1:
        print("""
        You are amazing! Your best score is {} guess.
        You have now completed the game.
        """.format(best_score[-1]))
    elif best_score[-1] == 0:
        if len(best_score) > 1:
            print("""
            You have successfully quit the game. Your best score was {} guesses.
            """.format(best_score[-2]))
        else:
            print("You have successfully quit the game.")
    else:
        print("\n Your best score is {} guesses.".format(best_score[-1]))
        play_game = input("Would you like to play again? (Y)es or (N)o: ")
        play_game_option(play_game)


def start_game():
    solution.append(random.randint(1, 10))
    while True:
        try:
            guess = input("What number would you like to try (1-10):  ")
            if guess.lower() == "q":
                guesses.clear()
                clear_game()
                break
            else:
                guess = int(guess)
            if guess > 10 or guess < 1:
                raise ValueError()
        except ValueError:
            print("You must enter a number between (1-10).")
        else:
            if guess > solution[0]:
                add_to_guesses(guess)
                print("The hidden number is lower then {}.".format(guess))
                continue
            elif guess < solution[0]:
                add_to_guesses(guess)
                print("The hidden number is higher then {}.".format(guess))
                continue
            elif guess == solution[0]:
                add_to_guesses(guess)
                if len(guesses) == 1:
                    print("\n Wow!! Lucky guess. You have found the hidden number on your first try!!!")
                    clear_game()
                    break
                else:
                    print(" \n Good game. You have found the hidden number in {} tries!!!".format(len(guesses)))
                    clear_game()
                    break
    end_game()


print("""
-----------------------------
Welcome to the Guessing Game!
-----------------------------
""")
print("""
The Game:
* You are to find the hidden number by entering your guess number between 1 and 10 when prompted.
* You may also enter the letter 'Q' for quit at any time to quit the game.
* You may also choose to compete for a best score in which the game will end if the hidden number is found on your first try.
""")
player_name = input("Please enter your name:  ")
play_game = input("Hi {}. Are you ready to begin? (Y)es or (N)o:  ".format(player_name))
play_game_option(play_game)


print("""
Have a good day {}.
Come back and play anytime.
""".format(player_name))

# if __name__ == '__main__':
#     # Kick off the program by calling the start_game function.
#     start_game()
