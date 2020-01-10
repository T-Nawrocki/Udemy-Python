# tkinter provides access to the tk widget toolkit
# this is a toolkit which lets you make gui programs
#
# the toolkit was designed for a language called TCL
# this module essentially takes that and interprets between python and TCL,
# but we don't need to worry about that directly
# what it does mean is that the documentation isn't great

try:
    import tkinter
except ImportError:  # python 2 version uses a different (capitalised) module name
    import Tkinter as tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

tkinter._test()  # creates a test gui

# defines window, with some properties
main_window = tkinter.Tk()
main_window.title("Hello World")
main_window.geometry("640x480+200+200")  # window size and location on the screen

main_window.mainloop()  # opens the window by handing control over to tk to begin doing its event handling
