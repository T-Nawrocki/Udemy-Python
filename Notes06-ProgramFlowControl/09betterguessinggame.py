# lecture 51

import random  # a module which ships with python, contains functions to generate random values

lowest = 1  # change to change lowest possible guess/answer
highest = 10  # change to change highest possible guess/answer
answer = random.randint(lowest, highest)


def get_input():
    guess = input(f"Guess a number between 1 and {highest}: ")

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

while current_guess != answer:
    if current_guess < answer:
        print("Too low! Try again.")
        current_guess = get_input()
    elif current_guess > answer:
        print("Too high! Try again.")
        current_guess = get_input()

print(f"Yes! The answer is {answer}.")
