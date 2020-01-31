# lecture 58

# in python 3, range is a data type, but in python 2 it was just a function

print(range(100))  # prints the range object, not the elements of the range

my_list = list(range(10))  # converts range to list
print(my_list)  # prints list object

# ranges are very memory-efficient—a wider range doesn't take up more memory.
# this is different to lists—a list with more elements takes up more memory.
# so be careful when changing ranges to lists

my_string = "abcdefghijklmnopqrstuvwxyz"
print(my_string.index("e"))  # sequence.index(element) returns the index of that element within the sequence
print(my_string[4])

small_decimals = range(10)
print(small_decimals)
print(small_decimals.index(3))

odd = range(1, 100000, 2)
print(odd)
print(odd[15234])  # very quick to calculate, given memory efficiency of ranges

# ranges can be sliced, like strings

my_range = small_decimals[::2]
print(my_range)
print(my_range.index(4))

decimals = range(100)
my_range = decimals[3:40:3]
print(my_range == range(3, 40, 3))  # ranges with same elements are equivalent
print(range(0, 5, 2) == range(0, 6, 2))  # returns True because the sequence returned is equivalent
# so comparing ranges with == tests the output sequence, not the definition

r = range(10)
for i in r[::-1]:
    print(i)  # negative slice is a quick way to process a range in reverse
