# Dictionaries and Sets are both UNORDERED collections which guarantee no duplicates

# Sets are similar to lists in that they are designed to store similar items
# But you cannot access a particular item from a set using an index, because the collection is unordered

# Dictionaries are a collection of key-value pairs
# The key is how you access the values, rather than an index

fruit = {"orange": "a round citrus fruit",
         "apple": "good for making cider",
         "lemon": "a rugby ball shaped citrus fruit",
         "grape": "a small sweet fruit which grows in bunches",
         "lime": "a sour, green citrus fruit"}

print(fruit)  # prints the dictionary object
print(fruit["grape"])  # prints the value of the element of fruit with key "grape"

# keys must be unique, but values do not

bike = {
    "make": "Honda",
    "model": "250 Dream",
    "colour": "red",
    "engine_size": 250
}

print(bike["engine_size"])  # values do not need to be the same type
print(bike["colour"])

# keys can be different types too, but they must be immutable (so a tuple can be a key, but a list cannot)

fruit["pear"] = "some sort of weird apple"  # you can append elements to the dictionary,
# but there's no specific method beyond binding the value like this
print(fruit)

# binding a value to an existing key REPLACES the value, rather than creating a new entry
# this is because keys must be unique
fruit["pear"] = "good for making perry"
print(fruit)

# del is the operator to remove an entry from a dictionary
del fruit["lemon"]
print(fruit)
# del is much more powerful than this example indicates
# if you forget to include the key, it will delete the dictionary itself
# so use with care

# # .clear() removes the contents of a dictionary, but the dictionary object remains
# fruit.clear()
# print(fruit)

# print(fruit["tomato"])  # produces a KeyError, because the key does not exist within this dictionary

while True:
    dict_key = input("Please enter a fruit, or type 'quit' to exit: ")
    if dict_key == "quit":
        break
    if dict_key in fruit:
        description = fruit.get(dict_key)  # .get(arg) is a method to retrieve the value at a key
        # the important difference is that it doesn't return an error if there isn't anything there
        # instead it returns None
        print(description)
    else:
        print(f"{dict_key} does not appear in the dictionary")


