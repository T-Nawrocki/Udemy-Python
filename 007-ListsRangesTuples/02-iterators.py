# lecture 57

# iterators are an object that represent a stream of data
# they return the data in the stream one element at a time

# iterable objects are objects whihc support iteration
# strings and lists are examples of iterable objects

string = "1234567890"
for char in string:
    print(char)
# what is happening here is that an iterator is created for the string
# the for loop then uses that iterator to execute a block of code (here, print())
# when the last element is reached, the iterator returns an error and the for loop terminates
# note that the for loop handles the error so nothing goes wrong on this end

my_iterator = iter(string)  # manually creates an iterator, rather than implicitly doing it with a for loop
print(my_iterator)  # note that we're printing the iterator object itself, not the data stream
print(next(my_iterator))  # prints the next value in the data stream of my_iterator
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
# print(next(my_iterator))  # causes an error, because we've reached the end of the data stream

print("""
==========
""")

for char in string:
    print(char)

for char in iter(string):  # this does the exact same thing as the loop above,
                           # only this is what's ACTUALLY happening in both
    print(char)
