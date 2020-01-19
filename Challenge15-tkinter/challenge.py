# Write a GUI program to create a simple calculator
# layout that looks like the screenshot.
#
# Try to be as Pythonic as possible - it's ok if you
# end up writing repeated Button and Grid statements,
# but consider using lists and a for loop.
#
# There is no need to store the buttons in variables.
#
# As an optional extra, refer to the documentation to
# work out how to use minsize() to prevent your window
# from being shrunk so that the widgets vanish from view.
#
# Hint: You may want to use the widgets .winfo_height() and
# winfo_width() methods, in which case you should know that
# they will not return the correct results unless the window
# has been forced to draw the widgets by calling its .update()
# method first.
#
# If you are using Windows you will probably find that the
# width is already constrained and can't be resized too small.
# The height will still need to be constrained, though.

import tkinter

# define main window
main_window = tkinter.Tk()
main_window.title("Calculator")
main_window.geometry("240x240+500+500")
main_window["padx"] = 8
main_window["pady"] = 8

# define grid
# 2 columns, 3 rows
# final column and row are just padding, so that when expanding the actual calculator elements stay mostly the same
main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1, weight=1000)  # final column is just visual padding
main_window.rowconfigure(0, weight=1)
main_window.rowconfigure(1, weight=5)
main_window.rowconfigure(2, weight=1000)  # final row is just visual padding

# display bar
display_bar = tkinter.Entry(main_window)
display_bar.grid(column=0, row=0, sticky="ew")

# button frame
button_frame = tkinter.Frame(main_window)
button_frame.grid(column=0, row=1, sticky="news", pady=2)

for i in range(0, 3):
    button_frame.columnconfigure(i, weight=1)
for i in range(0, 4):
    button_frame.rowconfigure(i, weight=1)

# dictionary of buttons text and coordinates
button_list = {
    "C": (0, 0),
    "CE": (1, 0),
    "7": (0, 1),
    "8": (1, 1),
    "9": (2, 1),
    "+": (3, 1),
    "4": (0, 2),
    "5": (1, 2),
    "6": (2, 2),
    "-": (3, 2),
    "1": (0, 3),
    "2": (1, 3),
    "3": (2, 3),
    "*": (3, 3),
    "0": (0, 4),
    "=": (1, 4),
    "/": (3, 4)
}

# generate buttons from dictionary
# special case for = button which must be double wide
for key in button_list.keys():
    if key == "=":
        tkinter.Button(button_frame, text=key).grid(
            column=button_list[key][0], row=button_list[key][1], sticky="ew", columnspan=2, padx=1, pady=1)
    else:
        tkinter.Button(button_frame, text=key).grid(
            column=button_list[key][0], row=button_list[key][1], sticky="ew", padx=1, pady=1)


main_window.update()  # updates window to make sure widgets have ben drawn
# sets minimum size to button frame width and button frame + displaybar height
main_window.minsize(button_frame.winfo_width(), (button_frame.winfo_height() + display_bar.winfo_height()))

main_window.mainloop()
