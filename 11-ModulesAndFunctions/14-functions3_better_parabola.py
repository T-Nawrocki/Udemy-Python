# this program builds on the one we build in 13-functions2_parabola.py
# in that one, our parabola function just defined a parabola, but only for a single value
# we still had  to do a separate for loop to call the function on the range of values we wish to plot
# this program will enhance the parabola function so we only need to pass in arguments for
# size of parabola and canvas, and then the function draws the parabola

# we will also add a function to plot a circle as well

import tkinter
import math


def draw_axes(canvas):
    canvas.update()
    x_origin = canvas.winfo_width() / 2
    y_origin = canvas.winfo_height() / 2
    canvas.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    canvas.create_line(-x_origin, 0, x_origin, 0, fill="black")
    canvas.create_line(0, y_origin, 0, -y_origin, fill="black")


def plot(canvas, x, y, colour):
    canvas.create_line(x, -y, x + 1, -y + 1, fill=colour)  # negative y because screen coordinates increase down not up


def parabola(canvas, size, colour="red"):
    for x in range(size + 1):  # more efficient to calculate y for positive x
        y = (x ** 2) / size    # and then plot twice
        plot(canvas, x, y, colour)     # than to calculate for positive and negative x
        plot(canvas, -x, y, colour)    # and plot once


# because a circle is symmetrical on x and y, we only need to calculate a quarter of the circle
# we can then use that calculation to plot the other three quarters
# ========================================
# arguments are: the canvas on which to plot the circle; radius; centre x coordinate; centre y coordinate
# ========================================
# we use x_origin * 100 and (x_origin + radius) * 100 because we're not plotting non-integer values
# which means that the east-west edges can look a bit sparse
# so we fix that by plotting 100 times as many points as we "need"
# but that means we do need to do i /= 100 before performing our plot calculations
# ========================================
# So, the calculation for the positive quarter (bottom right) is:
# y = y origin + square root (r**2 - distance from x origin**2)
# Don't need to know the algebra really, because that's not the point of this exercise
# ========================================
# after we've calculated the values for the positive quarter of the circle, we can start plotting
# first plot with basic x and y (plots +x, +y)
# then plot +x, -y (need to minus 2 * y_origin to make it negative—can't just use -y because y_origin may be different)
# then plot -x, +y (as above, only minus 2 * x_origin)
# finally, plot -x, -y
def circle(canvas, radius, x_origin, y_origin, colour="red"):
    for x in range(x_origin * 100, (x_origin + radius) * 100):
        x /= 100
        y = y_origin + (math.sqrt(radius ** 2 - ((x - x_origin) ** 2)))
        plot(canvas, x, y, colour)
        plot(canvas, x, (2 * y_origin) - y, colour)
        plot(canvas, (2 * x_origin) - x, y, colour)
        plot(canvas, (2 * x_origin) - x, (2 * y_origin) - y, colour)


# a cleaner circle function, using the create_oval method of the Canvas widget
# circle() was a good exercise, but this is so much more efficient and uses a dedicated tool
def clean_circle(canvas, top_left_x, top_left_y, bottom_right_x, bottom_right_y, colour="red"):
    canvas.create_oval(top_left_x, top_left_y, bottom_right_x, bottom_right_y, outline=colour, width=2)


main_window = tkinter.Tk()
main_window.title("Parabola 2")
main_window.geometry("640x480")

graph_canvas = tkinter.Canvas(main_window, width=640, height=480)
graph_canvas.grid(column=0, row=0)
draw_axes(graph_canvas)

parabola(graph_canvas, 240)
circle(graph_canvas, 100, 0, 0, "green")
clean_circle(graph_canvas, -50, -50, 50, 50, "blue")

main_window.mainloop()
