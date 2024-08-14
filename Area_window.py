from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


def show_main_window(self):
    self.deiconify()


def Area_Window(main_window):
    # Window dimensions
    area_window = Toplevel()
    area_window.title("Area")
    area_window.geometry("600x350")

    # icon
    image = Image.open("./icons/arrow_back_1.png")
    image = image.resize((25, 25), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    area_window.photo = photo

    # BODY
    exit_button = ttk.Button(area_window, image=photo, compound=CENTER, width=2, command=lambda: [area_window.destroy(), show_main_window(main_window)])
    exit_button.place(x=10, y=10, anchor="nw")
