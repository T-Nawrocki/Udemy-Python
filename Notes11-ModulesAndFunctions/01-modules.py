# modules are like libraries from C#—premade code sets which are not designed to do anything independently, but instead
# can be used by other programs as a toolkit for whatever purpose they're designed for.

# incidentally, a python file which is intended to be executed independantly (in contrast to a module),
# is called a script in a lot of the documentation

# we've already seen a couple of external modules in our import operations for input/output and rng

# this is a module based on the educational language "logo" from the 90s
# it was to let children control a turtle on the screen, making it follow a pen which they move
import turtle

from time import sleep  # contains functions for interacting iwth time. Explicitly importing a single function

turtle.forward(150)  # the highlighting error here is a bug in intellij's syntax highlighting
turtle.right(120)     # it's just that intellij has trouble importing certain modules properly
turtle.forward(150)  # you can suppress them on a case-by-case basis or remove all warnings for the module altogether

sleep(4)  # pauses the program for 4 seconds (note we don't need time.sleep because sleep was explicitly imported)

turtle.right(120)
turtle.forward(150)

turtle.done()  # holds on current screen until window is closed


