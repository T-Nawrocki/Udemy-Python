# lecture 45

# for loops iterate through a sequence,
# bind each of the elements of that sequence to a variable in turn,
# and then executes a code block based on that binding
for i in range(1,21):
    print(f"i = {i}")

print("""
========
""")

# can use a for loop to index a sequence
number = "12,345,678,901,234,567,890"
for i in range(0, (len(number))):  # len() = length of argument
# note how above you don't need to do len(number) - 1, because the upper bound is not included in the range itself
    print(number[i])

print("""
========
""")

# removing separators
# because a string is a sequence, you can use a for loop to iterate over the characters
for char in number:
    if char in "1234567890":
        print(char,end="")  # end= defines what the printed string should end with. Default is \n
print()

# to convert the string number to int, clean it as above, and then convert to int
# need to first initialise a contained for the chars as we add them in the for loop
cleaned_number = ""
for char in number:
    if char in "1234567890":
        cleaned_number += char
number_as_int = int(cleaned_number)
print(f"The number is {number_as_int}, and "
      f"{number_as_int} + 74839202091819235401 = {number_as_int + 74839202091819235401}")

