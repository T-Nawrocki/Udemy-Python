# updating values stored in a shelf:
import shelve

blt = ["bacon", "lettuce", "tomato", "bread"]
beans_on_toast = ["beans", "bread"]
scrambled_eggs = ["eggs", "butter", "milk"]
soup = ["tin of soup"]
pasta = ["pasta", "cheese"]

with shelve.open("recipes") as recipes:
    recipes["blt"] = blt
    recipes["beans on toast"] = beans_on_toast
    recipes["scrambled eggs"] = scrambled_eggs
    recipes["pasta"] = pasta
    recipes["soup"] = soup

    for snack in recipes:
        print(snack, recipes[snack])

    print("=" * 40)

    # just using .append() won't work, because although we have appended data to the list,
    # there has been no trigger to have the shelf write the updated data to a file
    # this keeps disc access to a minimum, for performance reasons, however it's inconvenient here
    if "butter" not in recipes["blt"]:  # do not want to append again if we run program a second time
        recipes["blt"].append("butter")
    if "tomato" not in recipes["pasta"]:
        recipes["pasta"].append("tomato")

    for snack in recipes:
        print(snack, recipes[snack])  # note blt and pasta are unchanged

    print("=" * 40)

    # we can get around this by using a temporary list to append the data, then write that temporary list to the shelf
    # this way we keep the performance benefits of working with objects in memory (as opposed to constantly reading
    # and writing to disc), but we have to compromise by rebinding the data to the key in the shelf
    if "butter" not in recipes["blt"]:
        temp_list = recipes["blt"]
        temp_list.append("butter")
        recipes["blt"] = temp_list

# alternatively, we can open the shelf with "writeback" set to True
# this is more elegant code, but can have MUCH more impact on memory, especially if you're making lots of changes
with shelve.open("recipes", writeback=True) as recipes:
    if "tomato" not in recipes["pasta"]:
        recipes["pasta"].append("tomato")

    for snack in recipes:
        print(snack, recipes[snack])

    print("=" * 40)

# final note: shelve may not always be appropriate for your project
# objects are pickled when shelving, and unpickled when unshelved, which may impose a significant performance overhead
# especially when the data is complex
# also, as we've seen pickling uses OS-specific protocols, so shelves are often not the best solution for cross-platform
# applications which need to take their data with htem when they move between platforms.
# pickling protocols are also (as discussed previously), not secure, so distribution over the internet is unsuitable
# for any application using shelves
