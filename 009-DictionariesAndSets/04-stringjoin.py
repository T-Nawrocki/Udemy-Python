# brief aside on the string.join() method

# recall that strings are immutable
# as a result, it's not efficient to concatenate strings in a loop
# this is because each time you concatenate, the new concatenated string needs to be created from scratch

# string.join() is a solution to this
# it takes a sequence and produces a string from it
# the items in the new string are separated by the string that join was called upon

my_list = ["a", "b", "c", "d"]
new_string = ""

# # inefficient method, concatenating everything. Each time through the loop re-creates new_string
# for c in my_list:
#     new_string += f"{c}, "

# using .join, there's no need for a loop
new_string = ", ".join(my_list)
print(new_string)

# any sequence can be joined in this way, not just a list
# so for example, with another string:
my_string = "abcde"
new_string = ", ".join(my_string)
print(new_string)