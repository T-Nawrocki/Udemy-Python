# Create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alphabetical order.
#
# You can either enter the text from the keyboard or
# initialise a string variable with the string.

vowels = frozenset("aeiou")  # use frozenset rather than set because this is fixed, so we don't want to let this change
user_input = input("Enter a string: ")

non_vowels = []
for char in user_input:
    if char not in vowels:
        non_vowels += char
non_vowels.sort()

print(", ".join(non_vowels))
