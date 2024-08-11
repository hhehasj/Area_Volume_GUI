from tkinter import *
from tkinter import ttk


def show_main_window(self):
    self.deiconify()


def Area_Window(main_window):
    # Window dimensions
    area_window = Toplevel()
    area_window.title("Area")
    area_window.geometry("600x350")

    # BODY
    exit_button = ttk.Button(area_window, text="EXIT", width=10, command=lambda: [area_window.destroy(), show_main_window(main_window)])
    exit_button.place(x=150, y=150, anchor="center")