# a map, represented as a dictionary
# basic layout of the map is as follows (with north being ^:

#       -----> 5. Forest
#       |         ^
#       |         |
#       v         v
#   2. Hill <-- 1. Road <-> 3. Building
#       ^         ^
#       |         |
#       |         v
#       ---- 4. Valley

# "quit" (Q) must be available anywhere"

# ======================================
# CHALLENGE
# ======================================
# Modify the program so that the exits is a dictionary rather than a list,
# with the keys being the numbers of the locations and the values being
# dictionaries holding the exits (as they do at present). No change should
# be needed to the actual code.
#
# Once that is working, create another dictionary that contains words that
# players may use. These words will be the keys, and their values will be
# a single letter that the program can use to determine which way to go.
# ======================================


# dictionary of rooms, with room number-room description as the pairs
locations = {0: "You are sitting in front of a computer learning Python.",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building , a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

input_equivalents = {"NORTH": "N",
                     "GO NORTH": "N",
                     "EAST": "E",
                     "GO EAST": "E",
                     "SOUTH": "S",
                     "GO SOUTH": "S",
                     "WEST": "W",
                     "GO WEST": "W",
                     "QUIT": "Q",
                     "EXIT": "Q"}

# dictionary of dictionaries
# the keys are the room number, the values are dictionaries of the available exits for that room
exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

current_location = 1  # start at room 1

while True:  # use while True because we want the game to continue indefinitely until we give it the quit instruction

    # comma separates list of available exits by calling .keys() of the exits of the current
    # room (exits at key current_location), and then using .join() to combine into a string
    available_exits = ", ". join(exits[current_location].keys())

    print(locations[current_location])  # print value of current room in locations dictionary (ie room description)

    if current_location == 0:  # room 0 is the "quit" instruction, so here we break the loop, ending the game
        break

    # gets input for direction to move (using .upper() to make sure lower-case input
    # still matches keys from exits dictionaries)
    direction = input(f"Available exists are {available_exits}: ").upper()

    print()  # just a separator

    if len(direction) == 1:
        # if the input provided == one of the keys from the exits dictionary at current room's key,
        # change current location to the value of that key (ie the room that direction points to)
        if direction in exits[current_location]:
            # exits[current_location][direction] = value at the "direction" key
            # of the dictionary which is the value at key "current_location" of exits
            current_location = exits[current_location][direction]
        else:  # if input provided doesn't match any key of the current room exits dictionary, print an error
            print("You cannot go in that direction.")
    elif direction in input_equivalents:
        current_location = exits[current_location][input_equivalents[direction]]
    else:
        print("You cannot go in that direction.")
