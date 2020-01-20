import tkinter


# defines a parabola function
def parabola(x):
    y = (x ** 2) / 100  # / 100 to keep things from going off the screen, as  values are far greater than screen space
    return y


# defines a "draw axes" function
def draw_axes(canvas):
    canvas.update()  # update the canvas, so we can access width and height
    x_origin = canvas.winfo_width() / 2
    y_origin = canvas.winfo_height() / 2
    # scrollregion is a widget that forms a box with a corner at -x_origin, -y_origin, & the other at x_origin, y_origin
    canvas.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    canvas.create_line(-x_origin, 0, x_origin, 0, fill="black")  # draws a line between -x_origin and x_origin
    canvas.create_line(0, y_origin, 0, -y_origin, fill="black")  # draws a line between -y_origin and y_origin


# defines function to plot a curve
def plot(canvas, x, y):
    canvas.create_line(x, y, x + 1, y + 1, fill="red")


# main window
main_window = tkinter.Tk()
main_window.title("Parabola")
main_window.geometry("640x480")

# canvas is a widget which lets you draw basic shapes, curves and text
canvas = tkinter.Canvas(main_window, width=640, height=480)
canvas.grid(row=0, column=0)

draw_axes(canvas)

for x in range(-100, 101):
    y = parabola(x)
    plot(canvas, x, -y)  # - y because screen y increases downwards, but traditional graphing has y increasing upwards
    print(f"x = {x}, y = {y}")

main_window.mainloop()
