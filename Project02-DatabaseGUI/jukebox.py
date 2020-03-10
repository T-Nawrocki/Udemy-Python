import sqlite3
import tkinter

conn = sqlite3.connect("music.db")


class App(tkinter.Tk):

    def __init__(self, *args, **kwargs):

        tkinter.Tk.__init__(self, *args, **kwargs)
        self.title("Jukebox")
        self.geometry("1280x720")

        self.contents = tkinter.Frame()
        self.contents.pack()

        self.load_grid(self.contents)
        self.load_widgets(self.contents)

    @staticmethod
    def load_grid(frame):
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.columnconfigure(2, weight=1)

    @staticmethod
    def load_widgets(frame):
        pass


if __name__ == '__main__':
    main_window = App()
    main_window.mainloop()

