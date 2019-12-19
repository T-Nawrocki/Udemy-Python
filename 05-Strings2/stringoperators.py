# contains materials from lecture 33

# these operators can be used on any Sequence type

# Python has 5 sequence types:
#   string
#   list
#   tuple
#   range
#   bytes and bytearray (which are basically one type)
# a sequence is an ordered set of elements

# not all sequences can be concatenated (ranges cannot be, for example)

string1 = "he's "
string2 = "probably "
string3 = "pining "
string4 = "for the "
string5 = "fjords"
print(string1 + string2 + string3 + string4 + string5)  # concatenation

print("Hello " * 5)  # can multiply sequences (except ranges)

# operator precedence still applies:
print("Hello " * (5 + 4))  # would produce an error without internal brackets, because can't + string and int

today = "friday"
print("day" in today)  # True (in is the operator to check if a sequence contains the other argument)
print("thur" in today) # False

