import tkinter
import os

main_window = tkinter.Tk()
main_window.title("Advanced GUI Example")
main_window.geometry("640x480+600+200")

# configure row and column weights
main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1, weight=1)
main_window.columnconfigure(2, weight=3)
main_window.columnconfigure(3, weight=3)
main_window.columnconfigure(4, weight=3)
main_window.rowconfigure(0, weight=1)
main_window.rowconfigure(1, weight=10)
main_window.rowconfigure(2, weight=1)
main_window.rowconfigure(3, weight=3)
main_window.rowconfigure(4, weight=3)

# title label at top of window
# only widget in row 0
# spans 3 columns, starting at column 0
# will be centred in the three columns as this is default sticky value
# (sticky does not apply unless cell has weight—without weight text will be left-aligned)
title_label = tkinter.Label(main_window, text="Tkinter Grid Demo")
title_label.grid(column=0, row=0, columnspan=3)

# file list
# spans rows 1 and 2 of column 0
# fills whole of both cells
# populated with a list of options from the system directory
# (command to populate is different on different OS)
file_list = tkinter.Listbox(main_window)
file_list.grid(column=0, row=1, sticky="nsew", rowspan=2)  # sticky="nsew" stretches to fill in all 4 directions
file_list.config(border=2, relief="sunken")
for zone in os.listdir("C:/Windows/System32"):
    file_list.insert(tkinter.END, zone)  # inserts entry at the END of the listbox

# scrollbar for file list
# sits in cells (1,1) and (1,2)
# oriented vertically, stretched to fill vertically, and left-aligned
# has an event handler controlled by command=file_list.yview,
# which connects the scrollbar to the vertical position of file_list
list_scroll = tkinter.Scrollbar(main_window, orient=tkinter.VERTICAL, command=file_list.yview)
list_scroll.grid(column=1, row=1, sticky="nsw", rowspan=2)
file_list["yscrollcommand"] = list_scroll.set  # links position of scroll bar to position of file_list
                                               # (for when the user uses the scroll wheel, so scrollbar also follows)

# frame for radio buttons on right
# top- and left-aligned
# LabelFrame works like Frame, but allows a caption to be set using the text property
option_frame = tkinter.LabelFrame(main_window, text="File Details")
option_frame.grid(column=2, row=1, sticky="ne")

# radio buttons
# all three radio buttons share a single variable so that only one can be selected at a time
# tkinter.IntVar() is the control variable which will be used
# the radio buttons themselves are in option_frame
# when rbValue = value of a radio button, that button will show as selected
# and when selected, rbValue is set to the corresponding value
rbValue = tkinter.IntVar()
rbValue.set(3)  # sets default value of rbValue to 3
radio1 = tkinter.Radiobutton(option_frame, text="File Name", value=1, variable=rbValue)
radio2 = tkinter.Radiobutton(option_frame, text="Path", value=2, variable=rbValue)
radio3 = tkinter.Radiobutton(option_frame, text="Timestamp", value=3, variable=rbValue)
radio1.grid(column=0, row=0, sticky="w")
radio2.grid(column=0, row=1, sticky="w")
radio3.grid(column=0, row=2, sticky="w")

# result display—shows selected metadata from the file chosen according to the radiobutton choice
# consists of a Label and an Entry for the actual result
# both sit in the same cell of the grid, one top-aligned and the other bottom-aligned
result_label = tkinter.Label(main_window, text="Result")
result_label.grid(column=2, row=2, sticky="nw")
result_display = tkinter.Entry(main_window)  # entry are a text box
result_display.grid(column=2, row=2, sticky="sw")

# frame for time spinners
time_frame = tkinter.LabelFrame(main_window, text="Time")
time_frame.grid(column=0, row=3, sticky="new")
time_frame["padx"] = 36  # pads x axis by 36 (pady to pad y)
# time spinners
# spinners are Spinbox objects with width of 2 characters,
# and values restricted to a tuple of the valid range for that unit of time
# minute_spinner uses a different method to achieve the same thing, this time using from_ and to
# (need to use from_ not from, because from is a reserved word in python)
# generally, from_ and to are preferred wherever you can simply define start and end values
# whereas tuples are better where that's not possible (eg months)
hour_spinner = tkinter.Spinbox(time_frame, width=2, values=tuple(range(0, 24)))
minute_spinner = tkinter.Spinbox(time_frame, width=2, from_=0, to=59)
second_spinner = tkinter.Spinbox(time_frame, width=2, from_=0, to=59)
# adding the spinners to the grid
hour_spinner.grid(column=0, row=0)
tkinter.Label(time_frame, text=":").grid(column=1, row=0)  # adds : separator between spinners
minute_spinner.grid(column=2, row=0)
tkinter.Label(time_frame, text=":").grid(column=3, row=0)
second_spinner.grid(column=4, row=0)

# frame for date spinners
date_frame = tkinter.Frame(main_window)
date_frame.grid(column=0, row=4, sticky="new")
# date labels
day_label = tkinter.Label(date_frame, text="Day")
month_label = tkinter.Label(date_frame, text="Month")
year_label = tkinter.Label(date_frame, text="Year")
day_label.grid(column=0, row=0, sticky="w")
month_label.grid(column=1, row=0, sticky="w")
year_label.grid(column=2, row=0, sticky="w")
# date spinners
day_spinner = tkinter.Spinbox(date_frame, width=5, from_=1, to=31)
month_spinner = tkinter.Spinbox(date_frame, width=5, values=("Jan", "Feb", "Mar", "Apr", "May", "Jun",
                                                             "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"))
year_spinner = tkinter.Spinbox(date_frame, width=5, from_=2000, to=2099)
day_spinner.grid(column=0, row=1)
month_spinner.grid(column=1, row=1)
year_spinner.grid(column=2, row=1)


# ACTUALLY OPEN THE WINDOW AND RUN EVERYTHING
main_window.mainloop()

print(rbValue.get())  # prints rbValue (indicates radio button selection)