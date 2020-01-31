# Lecture 41

# indentation matters in python—without indentation, this would not work
# indentation is used instead of using brackets to delimit code blocks
for i in range(1, 13):
    print(f"{i} squared = {i ** 2}, and {i} cubed = {i ** 3}")
    print("calculation complete")

# a "Code Block" in python is a set of code whcih is executed as a unit
# a code block sits at (or beneath) a certain level of indentation
# so above, the print() calls are a single block
# a block can contain other blocks, which we'll get into shortly


