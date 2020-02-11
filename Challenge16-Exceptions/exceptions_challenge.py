# Write a short program to ask the user to type in two integer numbers, then print out their first number divided
# by the second. The program shouldn't crash, no matter what the user types in (although you don't have to worry
# about Ctrl keys).
# ==================================================

import sys


def get_int_input(i):
    """Requests number input, then returns that input as int (includes exception handling to request new input)"""
    try:
        n = input(f"Enter the {i} number: ")  # i is just an ordinal string passed when the function is called
    except EOFError:  # End of File error raised by Ctrl+D, which triggers End of File (no input left, exiting app).
        sys.exit(0)  # Exits the program with exit code 0 (normal exit)

    try:
        return int(n)
    except ValueError:
        print("That isn't a whole number, I can't use that. Please try again.")
        return get_int_input(i)


def divide(x, y):
    """Returns result of dividing two arguments (includes exception handling for divide by zero)"""
    try:
        return x / y
    except ZeroDivisionError:
        print(f"{x} / 0 is undefined. Go watch Numberphile videos to understand why, it's quite interesting.")


if __name__ == '__main__':
    print("This program will show the result of dividing the two numbers you enter.")
    a = get_int_input("first")
    b = get_int_input("second")

    # Using conditional to prevent this print happening if divide() returns None (ie, if divide() raises an exception)
    if divide(a, b):
        print(f"{a} / {b} = {divide(a, b)}")