# contains material from lecture 37

# string interpolation is an old way of formatting strings from Python 2
# good to understand how it works, but don't get used to it because it's being removed at some point

age = 26
print("I am %d years old" % age)

print("To insert a %s , use this syntax" % "string")
print("To insert a float, like %f, use this syntax" % 6.842)
print("Formatting precision etc is done like this: %60.50f" % (22 / 7))

# replacement is strictly one at a time, left to right. None of the flexibility you get from other methods
