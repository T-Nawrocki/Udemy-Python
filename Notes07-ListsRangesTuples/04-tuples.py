# lecture 60

# A tuple is an ordered set of data
# They are similar to lists, but unlike lists tuples are IMMUTABLE
# That means they can't be changed with .append() or similar

# You may have heard that, like lists are defined with [], tuples are defined with ()
# This is not the case. , separates the elements of a tuple. () are only used to disambiguate
t = "a", "b", "c"
print(t)  # prints tuple object
print("a", "b", "c")  # prints sequence of strings
print(("a", "b", "c"))  # prints tuple object—brackets only needed because print() also uses comma separators
# some people might prefer to use brackets universally for tuples, for consistency
# but you might work on code which does not so be aware of the possibility

betty = "Black Betty", "Caravan Palace", 2017
reality = "Your Reality", "Dan Salvato", 2017
landfill = "We are Happy Landfill", "Gorillaz", 2007

print(betty)  # prints whole tuple
print(betty[0])  # prints element 0 of tuple

# betty[0] = "Lone Digger"  # causes an error, because tuples are immutable
betty = "Lone Digger", betty[1], betty[2]  # can "change elements" by changing the variable
# so the object itself can't be changed, but you can create a new object
# based on the old one and bind the variable to the new one instead

# although it's not enforced, lists are intended to contain items of the same type
# in contrast, tuples are fully intended to support elements with different types

a = b = c = d = 12  # can bind multiple variables to same value at once
e, f = 12, 13  # can also do it like this to bind different values

# using this method, we can bind multiple variables to the values of a tuple
title, artist, year = landfill  # this is called UNPACKING the tuple
print(title)
print(artist)
print(year)

# tuples can be elements of other tuples
tracks = betty, reality, landfill
print(tracks)

##########

# although a tuple is immutable, it can contain mutable elements
# so if a tuple contains a list, the elements of hte list can be changed, even if the list itself cannot
