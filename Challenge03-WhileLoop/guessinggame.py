# Modify the program below to use a while loop to
# allow as many guesses as necessary.
#
# The program should let the player know whether to
# guess higher or lower, and should print a message
# when the guess is correct. A correct guess will
# terminate the program.
#
# As an optional extra, allow the player to quit by entering
# 0 (zero) for their guess.

##########

# I actually did this for the previous lecture, without realising it'd be the next challenge.
# so just copying that solution here, and then will add a quit mechanism
# (although I don't like using 0, so will use something else)

##########

import random  # a module which ships with python, contains functions to generate random values

lowest = 1  # change to change lowest possible guess/answer
highest = 10  # change to change highest possible guess/answer
answer = random.randint(lowest, highest)


def get_input():
    guess = input(f"Guess a number between 1 and {highest}, or type 'exit' to quit the program: ")

    if guess.lower() == "exit":
        return "exit"

    for char in guess:
        if char not in "1234567890":
            print("That is not a positive integer. Try again.")
            get_input()

    guess_as_int = int(guess)

    if not lowest <= guess_as_int:
        print(f"That guess is less than {lowest}. Try again.")
        get_input()
    elif not guess_as_int <= highest:
        print(f"That guess is more than {highest}. Try again")
        get_input()

    return guess_as_int


current_guess = get_input()

if current_guess == "exit":
    print("Okay, come back soon.")
else:
    while current_guess != answer:
        if current_guess < answer:
            print("Too low! Try again.")
            current_guess = get_input()
        elif current_guess > answer:
            print("Too high! Try again.")
            current_guess = get_input()

    print(f"Yes! The answer is {answer}.")
