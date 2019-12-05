# lecture 46

# for loops can be used with lists, as lists are another type of sequence
for state in ["not pining", "no more", "a stiff", "bereft of life"]:
    print(f"This parrot is {state}.")

# and similarly they work with ranges:
for i in range(0, 101, 5):  # the third argument is the step value
    print(i)

# embedded for loops iterate over the inner variable first, then the outer one
for i in range(1,13):
    for j in range(1,13):
        print(f"{i} * {j} = {i * j}")
    print("==========")
