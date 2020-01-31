# lecture 47

shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
for item in shopping_list:
    if item == "spam":
        continue  # continue exits the code block and resumes at the next iteration of the loop
    print(f"Buy {item}")

print("""
=====
""")

for item in shopping_list:
    if item == "spam":
        break  # break exits the entire loop at this point.
    print(f"Buy {item}")

print("""
=====
""")

for item in shopping_list:
    if item == "spam":
        continue
    print(f"Buy {item}")
else:  # for a loop, else runs a codeblock if the loop was permitted to complete
    print("That's the whole shopping list.")