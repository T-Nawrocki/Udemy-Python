# a drawback of pickling in some situations is that all the objects need to be loaded back into memory
# if you're dealing with a large object/large set of objects, loading everything back in might be a bad idea
# shelving is an alternative which fixes this

# a shelf is like a dictionary to hold the data you're shelving, but it's stored in a file rather than memory
# so we can think of shelves as a persistent dictionary

# the files are still pickled when saved, so all the same security concerns for pickling still apply here

import shelve

with shelve.open("shelf_test") as fruit:  # shelves are by nature read-write, so don't need to specify
    fruit["orange"] = "a sweet, orange, citrus fruit"
    fruit["apple"] = "baby cider"
    fruit["grape"] = "the way a soul communes with gods"
    fruit["lemon"] = "a dream we had five years from now"
    fruit["lime"] = "unbearable solemnity"

    print(fruit["lemon"])
    print(fruit["grape"])

# the shelf is created as a database, which is why here we have .bak, .dat and .dir files for the one shelf

# a major difference between shelves and dictionaries is that there is no shelf literal
# so you CAN'T create a shelf using:
# fruit = {"orange": "a sweet, orange, citrus fruit" ...}
# we have to do it like we've done above—create the shelf, then add values at each key manually
# if you try to do it the other way, you end up creating a dictionary within the python file, rather than making a shelf

print(fruit)  # fruit is a shelf object, not a dictionary or anything else
print("=" * 40)

# can update the value assigned to a key as follows:
with shelve.open("shelf_test") as fruit:
    fruit["lime"] = "created anew each morning"

    for snack in fruit:
        print(f"{snack}: {fruit[snack]}")

print("=" * 40)

with shelve.open("shelf_test") as fruit:
    while True:
        dict_key = input("Please enter a fruit, or type 'quit' to exit:")
        if dict_key.lower() == "quit":
            break

        # .get() does not return an error if the key doesn't exist
        # second argument sets a default if no key is found
        # default if second argument isn't used is "None"
        description = fruit.get(dict_key, "That fruit does not please me.")
        print(description)

print("=" * 40)

# remember the keys in your shelf are unsorted (although they may *show* as sorted on some operating systems)
# if we need to sort them to display or something, we can do this:
with shelve.open("shelf_test") as fruit:
    ordered_keys = list(fruit.keys())  # creates a list of the keys
    ordered_keys.sort()  # sorts the keys
    for f in ordered_keys:
        print(f"{f} = {fruit[f]}")

print("=" * 40)

with shelve.open("shelf_test") as fruit:
    for v in fruit.values():  # .values() creates a list of values
        print(v)
    print(fruit.values())

    for f in fruit.items():  # .items() creates a list of tuples for each key/value
        print(f)
    print(fruit.items())

    # actually, these are ValuesView and ItemsView objects, not lists.
    # these are view objects, which you will remember means they can't be altered,
    # they only give a window into another object

# minor final point—shelves can only take strings as their key, contrast to dictionaries which take any immutable object
