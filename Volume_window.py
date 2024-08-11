from tkinter import *
from tkinter import ttk


def show_main_window(self):
    self.deiconify()


def Volume_Window(main_window):
    # Window dimensions
    volume_window = Toplevel()
    volume_window.title("Volume")
    volume_window.geometry("600x350")

    # BODY
    exit_button = ttk.Button(volume_window, text="EXIT", width=10, command=lambda: [volume_window.destroy(), show_main_window(main_window)])
    exit_button.place(x=150, y=150, anchor="center")