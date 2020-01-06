import shelve

with shelve.open("locations") as locations:
    with shelve.open("vocabulary") as vocabulary:
        loc = "1"  # changed to string, because keys in a shelf must be strings
        while True:
            availableExits = ", ".join(locations[loc]["exits"].keys())

            print(locations[loc]["desc"])

            if loc == "0":
                break
            else:
                allExits = locations[loc]["exits"].copy()
                allExits.update(locations[loc]["namedExits"])

            direction = input("Available exits are " + availableExits).upper()
            print()

            # Parse the user input, using our vocabulary dictionary if necessary
            if len(direction) > 1:  # more than 1 letter, so check vocab
                words = direction.split()
                for word in words:
                    if word in vocabulary:   # does it contain a word we know?
                        direction = vocabulary[word]
                        break

            if direction in allExits:
                loc = str(allExits[direction])  # changed to convert to string, because keys in shelf must be strings
            else:
                print("You cannot go in that direction")
