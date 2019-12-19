# lecture 51

# while is another loop, like for
i = 0  # counter must be initialised first
while i < 6:
    print(f"i is now {i}")
    i += 1  # counter must be explicitly incremented (or some other way for the condition to become false/loop to break)
# you usually wouldn't use "while" like this, just to iterate through a range, because for is better for that

# while loops are much better for things which aren't just iterating through a sequence
# for example, things which need to happen continuously until a condition is met
available_exits = ["north", "east", "west"]
chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ")
    if chosen_exit == "quit":
        print("Fine, you don't want to escape? See if I care...")
        break  # break and continue still work just as with for
else:  # and unfortunately, so does else (creates a block that's only executed if the loop completes)
    print("Aren't you glad you got out of there.")
