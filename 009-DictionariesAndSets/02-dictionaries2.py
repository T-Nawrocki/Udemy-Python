fruit = {"orange": "a round citrus fruit",
         "apple": "good for making cider",
         "lemon": "a rugby ball shaped citrus fruit",
         "grape": "a small sweet fruit which grows in bunches",
         "lime": "a sour, green citrus fruit"}

while True:
    dict_key = input("Please enter a fruit or 'quit' to exit: ")
    if dict_key == "quit":
        break
    # sets a default value for dict.get(), if key does not exist
    description = fruit.get(dict_key, f"{dict_key} doesn't appear in this dictionary")
    print(description)

for snack in fruit:  # can iterate over elements of the dictionary
    print(fruit[snack])
    # output order will change each time because the dictionary is unordered
    # this is because the key is hashed—we will look at this later in the course
    # in short, they're basically a one-way function, which makes it very hard to reuse the exact same one
    # because the dictionary is created fresh each time we run the program, a different hash is used
    # which means we get different orders

# however, printing the dictionary many different times within the program will not change the order
# until we change the dictionary itself
for i in range(10):
    for snack in fruit:
        print(f"{snack} is {fruit[snack]}")
    print("-" * 40)

# ordered dictionaries do exist in the collections library, if you need it, but we'll cover that later
# (but in general, avoid using stuff you need to import from external libraries whenever you can,
# because it helps keep your program efficient)

# ordering tends to come up when you need to present the information in the dictionary for a human to look at
# so perhaps the best way to deal with this is to ignore ordering until that point where it becomes necessary
# at that point, we could create and sort a list with the keys/values, and then iterate over that to print it all out
ordered_keys = list(fruit.keys())  # creates a list of the keys
ordered_keys.sort()  # sorts keys a–z
for key in ordered_keys:
    print(f"{key} — {fruit[key]}")

# does the same thing with less code
ordered_keys = sorted(list(fruit.keys()))
for key in ordered_keys:
    print(f"{key} — {fruit[key]}")

# does the same thing with even less code
for key in sorted(fruit.keys()):
    print(f"{key} — {fruit[key]}")

# does the same thing with even less even less code:
for key in fruit:
    print(f"{key} — {fruit[key]}")

# .values() gets the values, in the same way .keys() gets keys
# but .values() is less efficient, so stick to .keys() where you can

# the objects returned by .keys() and .values() dict_key and dict_values objects respectively
# these are list-like objects
# these objects are called view objects, which means they update as the underlying dictionary object changes
# like a window into the dictionary
fruit_values = fruit.values()
print(fruit_values)
fruit["tomato"] = "a botanical fruit but a culinary vegetable"
print(fruit_values)  # we changed the dictionary, not the variable,
# but the result still updates because fruit.values() is a view object, and fruit_values is bound to that object

