# lectures 73 and 74

# sets are another unordered collection
# they work in a way that will be very familiar from set theory in maths

# sets cannot contain duplicates, like dictionary keys
# however, unlike dictionaries, values in a set are not accessed by a key
# you can think of them as like a collection of keys—
# they're similarly unique and hashed in the same way, and must be immutable

# sets are defined with {}, like dictionaries, but lack the : for a key-value pair
farm_animals = {"sheep", "cow", "pig"}
print(farm_animals)

# can also create a set using the set() constructor on another collection
wild_animal_list = ["lion", "tiger", "elephant"]
wild_animals = set(wild_animal_list)
print(wild_animals)

# .add() to add an element to the set
farm_animals.add("horse")
wild_animals.add("horse")

# need to use the set() constructor to create an empty set, because {} will create an empty dictionary
empty_set = set()
empty_dictionary = {}

# sets can be manipulated using union and intersection as you'd expect
even = set(range(0, 40, 2))
print(even)
print(f"There are {len(even)} even numbers in the even set")

squares_tuple = (1, 4, 9, 16, 25)
squares = set(squares_tuple)
print(squares)
print(f"There are {len(squares)} squares in the squares set")

combined_set = even.union(squares)  # obviously, this is exactly the same as squares.union(even)
print(combined_set)
print(f"There are {len(combined_set)} elements of the combined set")

even_squares = even.intersection(squares)
print(even_squares)
print(f"There are {len(even_squares)} even squares in the set")

# & can be used instead of .intersection()
print(even_squares == even & squares)
# | can be used instead of .union()
print(combined_set == even | squares)

# difference removes from one set the intersection of that set with another
even_without_squares = even.difference(squares)
print(even_without_squares)
print(f"There are {len(even_without_squares)} non-square evens in the set")
print(even_without_squares == even - squares)  # - can be used instead of .difference()

# symmetric difference returns union minus intersection
even_xor_square = even.symmetric_difference(squares)
print(even_xor_square)
print(f"There are {len(even_xor_square)} elements of the even xor square set")
print(even_xor_square == even ^ squares)  # ^ can be used instead of .symmetric_difference()

# .difference_update() does subtraction in place
# ie, it doesn't return the new set, but updates the set it's called upon to reflect the changes
# this is like how .sort() worked for lists etc
set_1 = {1, 2, 3, 4}
set_2 = {2, 4}
set_1.difference_update(set_2)
print(set_1)

# sorted() turns the set into a sorted list
set_3 = {5, 1, 2, 23, 1906, 7}
print(sorted(set_3))

# removing items from a set can be done using either .discard() or .remove()
# the difference between the two is that .remove() raises an error if the item to be removed doesn't exist
# whereas .discard() will not.
# which one to use will depend on whether you want to take a particular action if the item doesn't exist
# if so, you use .remove() in a try: except: block to use the exception raised to take other action
# if not, and you just want rid of it if it's there, .discard() is appropriate
set_3.discard(7)
print(set_3)
# set_3.remove(7)  # causes an error, because 7 has already been removed from the set
# print(set_3)

# set1.issubset(set2) and set1.issuperset(set2) check if set1 is a subset or superset of set2, respectively
set_a = {1, 2, 3, 4, 5}
set_b = {1, 2, 3}
print(set_a.issubset(set_b))  # False
print(set_a.issuperset(set_b))  # True

# frozen sets are an immutable set (can't be changed)
# this means that they can be used as a dictionary key, but also that they can be elements of other sets
odd = frozenset(range(1, 100, 2))
print(odd)
# odd.add(101)  # causes an error because frozensets have no .add() attribute.

