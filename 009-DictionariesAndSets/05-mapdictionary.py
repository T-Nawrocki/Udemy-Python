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

locations = {0: "You are sitting in front of a computer learning Python.",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building , a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

# list of dictionaries
exits = [{"Q": 0},
         {"W": 2, "E": 3, "N": 5, "S": 4, "Q":0},
         {"N": 5, "Q": 0},
         {"W": 1, "Q": 0},
         {"N": 1, "W": 2, "Q": 0},
         {"W": 2, "S": 1, "Q": 0}]

current_location = 1
while True:
    available_exits = ", ". join(exits[current_location].keys())

    print(locations[current_location])

    if current_location == 0:
        break

    direction = input(f"Available exists are {available_exits}").upper()
    print()
    if direction in exits[current_location]:
        current_location = exits[current_location][direction]
    else:
        print("You cannot go in that direction.")
