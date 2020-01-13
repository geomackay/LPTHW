"""Write a program where the computer randomly generates a number between 0 and 20.
The user needs to guess what the number is.
If the user guesses wrong, tell them their guess is either too high, or too low.
This will get you started with the random library if you haven't already used it."""

import random


def guessing_game():

    # Create machines number
    num = random.randint(0, 20)

    def user_attempt():
        # Prompt user for guess
        guess = int(input("Enter guess: "))
        checks_n_balances(guess)

    def checks_n_balances(guess):
        if num == guess:
            win_condition()
        if num > guess:
            print("Too Low!")
            user_attempt()
        if num < guess:
            print("Too High!")
            user_attempt()

    def win_condition():
        print("You Win!")

    print("Guess the number between 0 and 20")
    user_attempt()


guessing_game()
