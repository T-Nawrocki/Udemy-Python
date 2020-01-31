# Another example of recursion—a computer's file directory
# so after calling a function to list all objects in a directory,
# the function can call itself for each of those objects which is itself a directory
# (ie, get a list of all objects, and all objects contained within those objects, and so on)

import os

# the os module has a walk() function which goes through each subdirectory for you
listing = os.walk(".")  # returns path, subdirectories, and files for the directory passed
for root, directories, files in listing:
    print(f"ROOT: {root}")
    print("DIRECTORIES")
    for d in directories:
        print(f"\t{d}")
    print("FILES:")
    for file in files:
        print(f"\t{file}")
    print("=" * 40)

print()
print("=" * 40)
print("Now the homemade version...")
print("=" * 40)
print()


def list_directories(directory):
    """
    lists subdirectories of a directory, including sub-subdirectories etc
    this function just checks that the directory passed exists, then calls dir_list()
    which actually produces the subdirectory list
    """

    # can define functions within a function
    # makes sense to do that here because it's only used in this one function anyway
    def dir_list(d):
        nonlocal tab_stop  # similar to global keyword, but tab_stop isn't global, it's from a wider local scope
        files = os.listdir(d)
        for f in files:
            current_dir = os.path.join(d, f)
            if os.path.isdir(current_dir):
                print(("\t" * tab_stop) + "Directory " + f)
                tab_stop += 1
                dir_list(current_dir)
                tab_stop -= 1
            else:
                print(("\t" * tab_stop) + f)

    tab_stop = 0
    if os.path.exists(directory):
        print(f"Directory listing of {directory}:")
        dir_list(directory)
    else:
        print(f"{directory} does not exist.")


list_directories(".")
