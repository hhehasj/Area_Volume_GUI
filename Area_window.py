from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from widgets_of_frame import shape_widgets_area


def show_main_window(self):
    self.deiconify()


def Area_Window(main_window):
    # START
    area_window = Toplevel()
    area_window.title("Area")
    area_window.resizable(False, False)

    # WINDOW DIMENSIONS
    screen_width = area_window.winfo_screenwidth()  # Gets width of the screen
    screen_height = area_window.winfo_screenheight()  # Gets height of the screen
    center_x = int(screen_width/2 - 600/2)
    center_y = int(screen_height/2 - 350/2)

    area_window.geometry(f"600x350+{center_x}+{center_y}")

    # icon
    image = Image.open("./icons_and_photo/arrow_back_1.png")
    image = image.resize((25, 25), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    area_window.photo = photo

    # BODY
    exit_button = ttk.Button(area_window, image=photo, compound=CENTER, width=2, command=lambda: [area_window.destroy(), show_main_window(main_window)])
    exit_button.place(x=10, y=10, anchor="nw")

    shape_variable = StringVar()
    shape_combobox = ttk.Combobox(area_window, textvariable=shape_variable, font="Arial 12 bold")  # Combobox widget
    shape_combobox["values"] = ("Circle", "Square", "Rectangle", "Triangle", "Oval", "Semicircle")
    shape_combobox["state"] = "readonly"
    shape_combobox.place(x=300, y=100, anchor="center")

    def entries(event):
        selected_shape = shape_combobox.get()

        entry_frame = ttk.Frame(area_window, width=600, height=200)
        entry_frame.place(relx=0.5, rely=0.65, anchor="center")

        shape_widgets_area(entry_frame, selected_shape)
    shape_combobox.bind("<<ComboboxSelected>>", entries)

    # END
    style = ttk.Style()
    style.configure("TCombobox")

