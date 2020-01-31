import shelve

# note that changing the shelf name will create a second database when the program is run
with shelve.open("bike") as bike:
    bike["make"] = "Honda"
    bike["model"] = "250 Dream"
    bike["colour"] = "red"
    bike["engine_size"] = 250
    # similarly, changing a key that has been assigned (eg because of a typo) won't undo the old assignment when you
    # re-run the program—it will just assign the new key and leave the old one as it is
    # this is becauyse we're writing to a file, and haven't removed the data from that file

    for key in bike:
        print(key)  # note we have an "engin_size" key
    print("=" * 40)

    del bike["engin_size"]  # deletes key

    for key in bike:
        print(key)

