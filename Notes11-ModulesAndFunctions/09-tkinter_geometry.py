import tkinter

main_window = tkinter.Tk()
main_window.title("Geometry")
main_window.geometry("960x480+200+200")

# geometry can be controlled by geometry managers
# geometry managers control the locations and sizes widgets (gui elements) appear in the window

# there are three primary geometry managers
# the most useful is usually the grid manager
# however we're going to start with the pack manager, because that was the first one
# and it's generally the easiest one to learn to use

# note: everything in tk is a window
# objects are placed in a hierarchy
# so here, main_window is the root window,
# so everything else must be placed within it or within one of the child windows
# everything must have a parent window except the root window

# creates a label widget in the main window, with text "Hello World",
# then uses the pack manager to place it at the top of the window
label = tkinter.Label(main_window, text="Hello World")
label.pack(side="top")

# creates a canvas widget in the main window, sets it to have raised appearance and 1px border
# then uses pack manager to place it at the left of the window
# also using pack manager, sets the canvas to fill the height of the window
# note if you want to fill horizontally, you can't just change Y to X here
# you do that, but also you need to add expand=True as an argument to .pack
# this is because we've set the side to "left", so we're specifying X properties already
# if we changed the side to "top", we'd need expand=True for Y fill, but not for X
canvas = tkinter.Canvas(main_window, relief="raised", borderwidth=1)
canvas.pack(side="left", fill=tkinter.Y)

# widgets placed on the same side will be placed adjacent to each other in the order they're packed
button1 = tkinter.Button(main_window, text="button1")
button2 = tkinter.Button(main_window, text="button2")
button3 = tkinter.Button(main_window, text="button3")
button1.pack(side="left")
button2.pack(side="left")
button3.pack(side="left")

# you can change this behaviour by setting anchor to n/e/s/w
# however note that because we've packed the buttons to the left side of the window,
# anchor can only affect the vertical positioning (horizontal positioning is already set)
# the same would apply if we packed to a vertical position (we'd only be able to anchor horizontally)
button4 = tkinter.Button(main_window, text="button4")
button5 = tkinter.Button(main_window, text="button5")
button6 = tkinter.Button(main_window, text="button6")
button4.pack(side="left", anchor="n")
button5.pack(side="left", anchor="s")
button6.pack(side="left", anchor="e")

# frames are widgets whcih can be used to group other widgets and manipulate them together
# they're only really suitable for very simple layouts
rightFrame = tkinter.Frame(main_window)
rightFrame.pack(side="right", anchor="n", fill=tkinter.Y, expand=False)
canvas2 = tkinter.Canvas(rightFrame,relief="raised", borderwidth=1)
canvas2.pack(side="right", anchor="n")


main_window.mainloop()