# Write a small program to ask for a name and an age. When both values have been entered,
# check if the person is the right age to go on an 18-30 holiday (they must be over 18 and under 31).
# If they are, welcome them to the holiday, otherwise print a (polite) message refusing them entry.

name = input("What is your name? ")  # gets name input


def get_age_input():
    age_input = input("How old are you? ")  # gets age input

    # checks each char in age_input for any non-digit char
    # if it finds one, prints error, and returns false
    for char in age_input:
        if char not in "1234567890":
            print("Please type only numbers when asked for your age")
            return False

    return age_input  # if all chars are digits, returns age_input


age = int(get_age_input())  # calls get_age_input and assigns output to variable, converted to int

while not age:  # if input contained non-digit, age will be False, so repeat binding to input until valid input given
    age = int(get_age_input())

if 17 < age < 31:  # checks if age is within range, and prints relevant message in each case
    print(f"Congratulations, {name}, you are eligible for the 18–30 holiday!")
else:
    print(f"Sorry, {name}, you are outside the age range for this holiday.")

