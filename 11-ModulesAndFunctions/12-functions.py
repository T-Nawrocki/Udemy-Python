# functions are a block of reusable code to carry out a task
# functions contain their own scope, and are called by name
# functions may have any number of arguments
# functions may or may not return a value (will return None if not)
# methods are very similar to functions, except that they are associated with an object/class
# we will look at methods later when we look at classes


# define a function
def python_food():
    print("spam and eggs")


# call a function
python_food()
print(python_food())  # prints the result of the function, which in this case is None
                      # note that the function is still called before the print command is executed


# prints text centred on 80 characters width
def python_food_2():
    width = 80
    text = "Spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


python_food_2()


# does the same thing as python_food_2, but this time we can pass any text in and it'll be centred
# ====================================================
# parameter name is entirely up to you, so long as you don't use a term that's already reserved/defined
# technically, parameters are the placeholders in the definition of a function, while arguments are the
# actual values passed in the calling of the function, but in practice the terms are often used interchangeably
def centre_text(text):
    text = str(text)  # required to convert any non-text argument into a string, otherwise you get an error
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)


centre_text("literally any text at all")
centre_text("yet more text")
centre_text("a number oh wait no it's still text haha fooled you")
centre_text(123456)  # demonstrating that the function can handle non-string arguments


# this version of centre_text allows multiple arguments
# (the * character indicates any number of arguments are possible)
def centre_text_multiple(*args):
    for arg in args:
        text = str(arg)
        left_margin = (80 - len(text)) // 2
        print(" " * left_margin, text)


centre_text_multiple("this is the first text", "this is the second", 3, 4, "and this is the fifth and final text")


# provides all the functionality of print(), but centres text on 80 chars
# we achieve this using the named parameters from the print() function
# ctrl+click print() to see documentation with all the parameters
def centre_text_multi_argument(*args, sep=" ", end="\n", file=None, flush=False):
    text = ""
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text, end=end, file=file, flush=flush)


centre_text_multi_argument(1, 2, 3, 4, 5, "six", "seven", "eight", "nine", "ten", sep=";")
# can write centred text to file as you'd expect
with open("centred", mode="w") as centred_file:
    centre_text_multi_argument(1, 2, 3, 4, 5, "six", "seven", "eight", "nine", "ten", sep=";", file=centred_file)

