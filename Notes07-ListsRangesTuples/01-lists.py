# lecture 54 and 55

# lists are another sequence type, which we've already used a bit
# you can do to lists anything which can be done to any other type of sequence
# we've already used a lot of sequence operators, but here's a couple more

ip_address = input("Please enter an IP address: ")
print(f"There are {ip_address.count('.')} '.' characters in that IP address.")
# .count() finds the number of occurrences of an item in the sequence.

parrot_list = ["not pining", "no more", "a stiff", "bereft of life"]
parrot_list.append("an ex-parrot")  # .append() adds an element to the list
for state in parrot_list:
    print(f"This parrot is {state}")

even = [2, 4, 6, 8, 10]
odd = [1, 3, 5, 7, 9]
numbers = even + odd  # can merge lists like this, but they will be unsorted (elements of odd following even)
# .sort() does not create a new object, it operates on the existing object
# this means that you can't just call a sorted list by using list.sort()
# you instead use list.sort(), and then list itself will be sorted
numbers.sort()
print(numbers)
# this sort of behaviour is common in python for functions which manipulate objects
# ie they tend to manipulate the original object, rather than creating a new object for hte output
# you can get around this using the sorted() function on the list:
other_numbers = [5, 1, 4, 2, 3]
print(sorted(other_numbers))  # sorted() DOES create a new object.
# Python will treat this object as different to the original one

##########

# lists can be created by binding a variable as we've seen previously
# but they can also be created with a constructor, which we'll see more of when we look at classes
# for now, think of a constructor as a type of function which creates a list (or whatever else)
list_1 = []  # using variable binding
list_2 = list()  # using a constructor
if list_1 == list_2:
    print("These lists are equal—it doesn't matter how you created it")

# you can pass a single iterable argument to list() and it will create a
# list with each of the elements of the argument as elements of the list
list_3 = list("Like this")
print(list_3)

even = [2, 4, 6, 8]
another_even = even
another_even.sort(reverse=True)  # sorts in reverse
print(even)  # because another_even and even are bound to the same object, even is also sorted
# to avoid this, we can create a new object using list(), but pass even as an argument to it
third_even = list(even)
third_even.sort()
print(third_even)  # sorted to correct order
print(even)  # still reversed

# the is operator checks if the arguments refer to the same object
# (note this is different to =, which checks if the values are the same)
fourth_even = list(even)
print(f"even is another_even: {even is another_even}")
print(f"even is fourth_even: {even is fourth_even}")

##########

# lists can take other lists as their elements
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
numbers = [even, odd]
for number_set in numbers:
    print(number_set)
    for number in number_set:
        print(number, end=" ")
    print()
