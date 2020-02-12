# In this lecture we're building off the program written for the exceptions challenge.
# ==================================================

import sys


def get_int_input(i):
    """Requests number input, then returns that input as int (includes exception handling to request new input)"""

    while True:
        try:
            n = input(f"Enter the {i} number: ")  # i is just an ordinal string passed when the function is called
        except EOFError:  # End of File error raised by Ctrl+D, which triggers End of File (no input left, exiting app).
            sys.exit(0)  # Exits the program with exit code 0 (normal exit)
        else:
            print("Else clauses execute after the try clause successfully executes (ie no exceptions found). They're "
                  "often used to prevent accidentally catching exceptions we aren't trying to handle at this point. "
                  "Eg, in our banking example, we only want the transaction to fail if there is a problem with the "
                  "database changes themselves, and not (for example) if there is a display error for the date on the "
                  "website. An else clause would let us catch the transaction errors in our try an except clauses, and "
                  "then do everything else (like rendering the following page) afterwards, meaning that errors in "
                  "unrelated pieces of code won't cause the transaction to roll back.")
        finally:
            print("A finally clause always executes, regardless of whether an exception is raised. "
                  "That makes it a perfect place for performing necessary cleanup that needs to happen whenever "
                  "your program closes, through exceptions or otherwise (eg closing database connections).")

        try:
            return int(n)
        except ValueError:
            print("That isn't a whole number, I can't use that. Please try again.")


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