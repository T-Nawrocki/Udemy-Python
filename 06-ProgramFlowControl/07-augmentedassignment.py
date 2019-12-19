number = "1,234,567,890,098,765,543,210"
cleaned_number = ""

for char in number:
    if char in "1234567890":
        cleaned_number += char  # this is augmented assignment
# augmented assignments are a combination in a single operator of a binary operation and an assignment
# doing it this way, rather than cleaned_number = cleaned_number + char, is more efficient
# this is because python only calls the variable once, rather than twice
# in other languages, the two statements are exactly equivalent, so it doesn't make a difference
# but in python it's definitely better practice to do it this way, not just for clean code

number_as_int = int(cleaned_number)
print(f"The number is {number_as_int}.")

# augmented assignment operators are:
#   +=
#   -=
#   *=
#   /=
#   //= (int division)
#   **= (power of)
#   %= (modulo)
# (and some bitwise operator ones too)
