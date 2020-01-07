# Python's Standard Library is hte library which ships with Python
# it contains everything we use without explicitly importing anything,
# plus a bunch of modules you don't need to download as a separate package (eg shelve, random)

print(dir())  # dir() returns everything in the current program (including implicitly imported core modules)
# note that anything with an underscore at the start of its name is not intended to be changed
# private variables don't exist in Python (ie you cannot *prevent* external changes to variables in a module)
# but names starting with an underscore mark the *intent* that the variable be private to its module

# __builtins__ contains all built in functions and types in the core language
for m in dir(__builtins__):
    print(m)  # prints everything in __builtins__

import shelve
print(dir())
print(dir(shelve))

# some core modules are written in C, rather than python itself
# this is mostly for modules interacting with system io
# however some are written in python
# we can view source code in intellij using ctrl+click on module name (try this on shelve above)

help(shelve)  # prints a whole bunch of help, including a link to documentation
# help can be used on individual functions too, if those functions have built in help documentation
