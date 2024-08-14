from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


def show_main_window(self):
    self.deiconify()


def Volume_Window(main_window):
    # Window dimensions
    volume_window = Toplevel()
    volume_window.title("Volume")
    volume_window.geometry("600x350")

    # icon
    image = Image.open("./icons/arrow_back_1.png")
    image = image.resize((25, 25), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    volume_window.photo = photo

    # BODY
    exit_button = ttk.Button(volume_window, image=photo, width=2, compound=CENTER, command=lambda: [volume_window.destroy(), show_main_window(main_window)])
    exit_button.place(x=10, y=10, anchor="nw")
