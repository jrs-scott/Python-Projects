from tkinter import *
import tkinter as tk

import fileMover_ui # Importing the app UI, which calls the functions when prompted
import fileMover_func # Importing the app functions to be called

# Building the main tkinter frame for the app
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # Empty tkinter frame that the widgets sit in
        self.master = master
        self.master.title("Text File Transfer")
        self.master.geometry("{}x{}".format(520, 140))
        self.master.resizable(width=False, height=False)

        # Loading the widgets/UI for the app
        fileMover_ui.loadUI(self)

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
