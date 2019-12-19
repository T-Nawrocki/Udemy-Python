# serialising objects is a process that allows object to be saved to a file so they can be restored from the file later
# pickling is the way python does this

# when an object is pickled, it's written to a file in a format that contains the object's data, and data to allow
# the object to be recreated later

import pickle  # need this module to be able to pickle things

imelda = ("More Mayhem",
          "Imelda May",
          "2011",
          ((1, "Pulling the Rug"),
           (2, "Psycho"),
           (3, "Mayhem"),
           (4, "Kentish Town Waltz")))

with open("imelda.pickle", "wb") as pickle_file:
    pickle.dump(imelda, pickle_file)  # pickle.dump(arg1, arg2) is the write function, writing arg1 to arg2

# pickle files are python-specific—you can't open them in other editors or languages

# retrieving data is achieved with pickle.load()
with open("imelda.pickle", "rb") as imelda_pickled:
    imelda_2 = pickle.load(imelda_pickled)

print(imelda_2)

# many objects can be pickled in the same file
another_object = ["a", "list", "object"]
third_object = "one stringy boy"

with open("imelda.pickle", "wb") as pickle_file:
    pickle.dump(another_object, pickle_file)
    pickle.dump(third_object, pickle_file)
    pickle.dump(123456, pickle_file)  # you can dump objects which aren't bound to a variable

# must be read back in the same order they were put in, however
with open("imelda.pickle", "rb") as imelda_pickled:
    another_object_2 = pickle.load(imelda_pickled)
    third_object_2 = pickle.load(imelda_pickled)
    x = pickle.load(imelda_pickled)

print(another_object_2)
print(third_object_2)
print(x)

# when pickling, you can choose which protocol is used to pickle the object
# the most recent protocol is protocol 4, which pickles more objects than the previous iterations etc
# but protocols aren't backwards compatible, so you may have to use the previous protocols to interact with older code

# protocol is selected using the third argument of pickle.dump()
# so pickle.dump(arg1, arg2, protocol=0) will pickle arg1 to arg2 under protocol 0
# default if no protocol is specified is protocol 3 (which is available under all versions of python 3,
# but not backwards compatible with python 2)

# pickle.load() doesn't need a protocol specified because it works it out from the pickle file which already exists

# protocol=pickle.HIGHEST_PROTOCOL and protocol=pickle.DEFAULT_PROTOCOL set the
# appropriate protocol based on the instruction used

# pickling uses an unsecure protocol—NEVER UNPICKLE SOMETHING YOU CAN'T BE SURE YOU TRUST
# basically only use it for code you made yourself, unless you have very good reason otherwise
