# contains material from lecture 17 and 18

print("You can use double quotes or single quotes for strings")
print('Python does not care which')
print("Python's able to handle quotes within quotes")
print('So long as the "internal quotes" are not the same as the external ones')
print("Concatenation is" + " addition of strings to each other")

print()
print("\\ is an escape character")
print("This is because it's used for special characters\nlike new line characters\tand tab characters\n")
print("You can also use it to make Python \"ignore\" the other effects a character would usually have (eg end string)")

print("""Triple quotes ensure there's no need for any "Escape Characters" because the string is plain text only""")
print("""This includes
strings that have been
split
using linebreaks""")
print("""However, you can still \
undo this behaviour for linebreaks \
with an escape character""")

print(r"You can also make a string into plain text (or raw) by using "r" before the string")
print("However using \\ to escape is generally preferred style")

print()
greeting = "Hello"
name = input("Please enter your name ")
print(greeting, name)


