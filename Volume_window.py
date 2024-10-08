from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from widgets_of_frame import shape_widgets_volume


def show_main_window(self):
    self.deiconify()


def Volume_Window(main_window):
    # START
    volume_window = Toplevel()
    volume_window.title("Volume")
    volume_window.resizable(False, False)

    # WINDOW DIMENSIONS
    screen_width = volume_window.winfo_screenwidth()  # Gets width of the screen
    screen_height = volume_window.winfo_screenheight()  # Gets height of the screen
    center_x = int(screen_width / 2 - 600 / 2)
    center_y = int(screen_height / 2 - 350 / 2)

    volume_window.geometry(f"600x350+{center_x}+{center_y}")

    # icon
    image = Image.open("./icons_and_photo/arrow_back_1.png")
    image = image.resize((25, 25), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    volume_window.photo = photo

    # BODY
    exit_button = ttk.Button(volume_window, image=photo, width=2, compound=CENTER,
                             command=lambda: [volume_window.destroy(), show_main_window(main_window)])
    exit_button.place(x=10, y=10, anchor="nw")

    shape_variable = StringVar()
    shape_combobox = ttk.Combobox(volume_window, textvariable=shape_variable, font="Arial 12 bold")  # Combobox widget
    shape_combobox["values"] = ("Sphere", "Cube", "Cuboid", "Cylinder", "Cone", "Triangular Prism", "Triangular Pyramid", "Pyramid", "Hemisphere")
    shape_combobox["state"] = "readonly"
    shape_combobox.place(x=300, y=100, anchor="center")

    # this gets the chosen shape from the combobox
    def entries(event):
        selected_shape = shape_variable.get()

        entry_frame = ttk.Frame(volume_window, width=600, height=200)
        entry_frame.place(relx=0.5, rely=0.65, anchor="center")

        shape_widgets_volume(frame=entry_frame, shape=selected_shape)

    shape_combobox.bind("<<ComboboxSelected>>", entries)

