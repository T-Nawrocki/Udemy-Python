# Although Pack is very simple, and generally suitable for trivial layouts only, Place is even more straightforward

# the Place geometry manager uses it uses the absolute position of at least one window,
# and orients everything else relative to that position
# if you can't use absolute position (eg you don't know the size of screen you'll be using),
# this approach won't be suitable

# for anything more complex than incredibly basic layout, you want to use the Grid geometry manager
# it works by adding widgets to a grid

# the grid doesn't really exist until you start adding things to it
# however when you add something to the grid, its dimensions are automatically calculated

import tkinter

main_window = tkinter.Tk()
main_window.title("Hello World")
main_window.geometry("640x480-8-200")

label = tkinter.Label(main_window, text="Hello World")
label.grid(column=0, row=0)  # places this widget in cell 0, 0

left_frame = tkinter.Frame(main_window)
left_frame.grid(column=1, row=1)

canvas = tkinter.Canvas(left_frame, relief="raised", borderwidth=1)
canvas.grid(column=0, row=1)

right_frame = tkinter.Frame(main_window)
right_frame.grid(column=2, row=1, sticky="n")  # sticky property anchors widgets to the direction chosen
                                               # in this case, it's just making the contents (buttons)
                                               # top aligned rather than centred in this frame

button1 = tkinter.Button(right_frame, text="button1")
button2 = tkinter.Button(right_frame, text="button2")
button3 = tkinter.Button(right_frame, text="button3")
button1.grid(column=0, row=0)
button2.grid(column=0, row=1)
button3.grid(column=0, row=2)

# by default, the grid columns/rows are given the minimum weight they need to display their contents
# column/rowconfigure is a way to override this.
main_window.columnconfigure(0, weight=1)        # columnconfigure and grid_columnconfigure are identical
main_window.columnconfigure(1, weight=1)        # ie they literally call the exact same method
main_window.grid_columnconfigure(2, weight=1)   # ctrl+click columnconfigure to see for yourself

left_frame.config(relief="sunken", borderwidth=1)  # puts border around the frames for ease of visibility
right_frame.config(relief="sunken", borderwidth=1)
left_frame.grid(sticky="ns")  # vertically stretches frame
right_frame.grid(sticky="new") # horizontally stretches and vertically top-aligns frame

# weight is necessary to enable certain properties of widgets (eg sticky)
# so we cannot stretch the buttons using sticky because they haven't got weight set
right_frame.columnconfigure(0, weight=1)  # sets weight for button column
button1.grid(sticky="ew")  # stretches button to fill horizontally
button2.grid(sticky="ew")
button3.grid(sticky="ew")

main_window.mainloop()
