fruit = {"orange": "a round citrus fruit",
         "apple": "good for making cider",
         "lemon": "a rugby ball shaped citrus fruit",
         "grape": "a small sweet fruit which grows in bunches",
         "lime": "a sour, green citrus fruit"}

# another view object for lists is the dict_items object, created by the .items() method
# this object consists of key-value tuples
print(fruit.items())

f_tuple = tuple(fruit.items())  # converts the dict_items object to a true tuple
print(f_tuple)

# using the tuple we've created to print stuff out
for snack in f_tuple:
    item, description = snack
    print(f"{item} is {description}")

# we can go the other way, from a tuple to a dictionary, using the dict() constructor
print(dict(f_tuple))
