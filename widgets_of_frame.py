from tkinter import *
from tkinter import ttk
from math import pi, sqrt


def shape_widgets(frame, shape):
    def volume_of_sphere(event):
        radius = radius_variable.get()
        volume = round(4 * (pi * float(radius) ** 3) / 3, 2)
        volume_output_label = ttk.Label(frame, text=f"Volume: {volume}")
        volume_output_label.place(rely=0.3, relx=0.5, anchor="center")

    for widget in frame.winfo_children():
        widget.destroy()

    if shape == "Sphere":
        radius_label = ttk.Label(frame, text="Radius:")
        radius_label.place(rely=0.5, relx=0.1, anchor="center")

        radius_variable = StringVar()
        radius_entry = ttk.Entry(frame, textvariable=radius_variable)
        radius_entry.place(rely=0.5, relx=0.5, anchor="center")
        radius_entry.bind("<Return>", volume_of_sphere)

    elif shape == "Cube":
        length_label = ttk.Label(frame, text="Length:")
        length_variable = StringVar()
        length_entry = ttk.Entry(frame, textvariable=length_variable)

        length_label.place(rely=0.5, relx=0.1, anchor="center")
        length_entry.place(rely=0.5, relx=0.5, anchor="center")

        length_label.place(rely=0.5, relx=0.1, anchor="center")
        length_entry.place(rely=0.5, relx=0.5, anchor="center")
