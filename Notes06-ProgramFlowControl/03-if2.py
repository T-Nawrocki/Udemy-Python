age = int(input("How old are you? "))

if age >= 16 and age <= 65:  # logical and
    print("Time for the capitalist nightmare of employment!")

if 16 <= age <= 65:  # same behaviour as above
    print("Retirement is a myth.")

# logial operators: and, or, not
# &, |, ^, ~ are sort of logical operators, but only used as "bitwise" operators to perform binary operations on bits
# so ignore for now

# ========================

# Unlike other languages, there is no boolean data type in python
# True and False are constants instead.

x = "string"
if x:  # here, x will evaluate to True because it is nonzero/nonempty
    print("x is true")

# so any value will evaluate to true except the following:
#   False
#   None (a data type which ~= null)
#   0
#   0.0
#   [] (an empty list)
#   () (an empty tuple)
#   '' (an empty string)
#   "" (an empty string)
#   {{}} (an empty mapping)
#   a class which has been created to evaluate to false (we'll get to this later so don't worry about it yet)

x = input("Enter some text: ")
if x:
    print(f"You entered {x}")
else:
    print("You did not enter any text")
