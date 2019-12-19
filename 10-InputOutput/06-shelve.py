# a drawback of pickling in some situations is that all the objects need to be loaded back into memory
# if you're dealing with a large object/large set of objects, loading everything back in might be a bad idea
# shelving is an alternative which fixes this

# a shelf is like a dictionary to hold the data you're shelving, but it's stored in a file rather than memory
# so we can think of shelves as a persistent dictionary

# the files are still pickled when saved, so all the same security concerns for pickling still apply here

import shelve

with shelve.open("shelf-test") as fruit:  # shelves are by nature read-write, so don't need to specify
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
# if you try to do it the other way, you end up creating a dictoinary within the python file, rather than making a shelf
