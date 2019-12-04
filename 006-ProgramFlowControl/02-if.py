# Lecture 42, 43

name = input("Please enter your name: ")
age = int(input(f"How old are you, {name}? "))  # input will be string, so use int() to convert to number
# entering anything but a number will cause an error, but we'll deal with error handling later in the course
print(age)

if age >= 18:
    print("You are old enough to vote.")
else:
    print(f"You will be able to vote in {18 - age} years.")

print("""
===========
""")

print("Please guess a number between 1 and 10")
txt = input()
if txt not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
    print("That's not a number between 1 and 10")
else:
    guess = int(txt)
    if guess < 5:
        print("Too low!")
    elif guess > 5:
        print("Too high!")
    else:
        print("Yes, the answer is 5!")
