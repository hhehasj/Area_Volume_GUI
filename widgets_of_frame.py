from tkinter import *
from tkinter import ttk
from math import pi


def shape_widgets_volume(frame, shape):
    for widget in frame.winfo_children():
        widget.destroy()

    if shape == "Sphere":
        def volume_of_sphere(event):
            try:
                radius = radius_variable.get()
                volume = round(4 * (pi * float(radius) ** 3) / 3, 2)
                ttk.Label(frame, text=f"Volume:").place(rely=0.3, relx=0.25, anchor="center")
                display.config(text=f"{volume}")
            except ValueError:
                ttk.Label(frame, text=f"Volume:").place(rely=0.3, relx=0.25, anchor="center")
                display.config(text="Invalid input")

        ttk.Label(frame, text="Radius:").place(rely=0.1, relx=0.25, anchor="center")

        radius_variable = StringVar()
        radius_entry = ttk.Entry(frame, textvariable=radius_variable, font=("Helvetica", 12), width=20)
        radius_entry.place(rely=0.1, relx=0.5, anchor="center")

        # displaying the volume of sphere
        display = ttk.Label(frame, text="")
        display.place(rely=0.3, relx=0.5, anchor="center")

        radius_entry.bind("<Return>", volume_of_sphere)

    elif shape == "Cube":
        def volume_of_cube(event):
            try:
                length = length_variable.get()
                volume = float(length) ** 3
                ttk.Label(frame, text=f"Volume:").place(rely=0.3, relx=0.25, anchor="center")
                display.config(text=f"{volume}")
            except ValueError:
                ttk.Label(frame, text=f"Volume:").place(rely=0.3, relx=0.25, anchor="center")
                display.config(text="Invalid input")

        ttk.Label(frame, text="Length:").place(rely=0.1, relx=0.25, anchor="center")

        length_variable = StringVar()
        length_entry = ttk.Entry(frame, textvariable=length_variable, font=("Helvetica", 12), width=20)
        length_entry.place(rely=0.1, relx=0.5, anchor="center")

        # displaying the volume of cube
        display = ttk.Label(frame, text="")
        display.place(rely=0.3, relx=0.5, anchor="center")

        length_entry.bind("<Return>", volume_of_cube)

    elif shape == "Cuboid":
        def volume_of_cuboid(event):
            try:
                length = length_variable.get()
                width = width_variable.get()
                height = height_variable.get()
                volume = float(length) * float(width) * float(height)
                ttk.Label(frame, text=f"Volume:").place(rely=0.7, relx=0.25, anchor="center")
                display.config(text=f"{volume}")
            except ValueError:
                ttk.Label(frame, text=f"Volume:").place(rely=0.7, relx=0.25, anchor="center")
                display.config(text="Invalid input")

        ttk.Label(frame, text="Length:").place(rely=0.1, relx=0.25, anchor="center")
        ttk.Label(frame, text="Width:").place(rely=0.3, relx=0.25, anchor="center")
        ttk.Label(frame, text="Height:").place(rely=0.5, relx=0.25, anchor="center")

        length_variable = StringVar()
        width_variable = StringVar()
        height_variable = StringVar()

        length_entry = ttk.Entry(frame, textvariable=length_variable, font=("Helvetica", 12), width=20)
        width_entry = ttk.Entry(frame, textvariable=width_variable, font=("Helvetica", 12), width=20)
        height_entry = ttk.Entry(frame, textvariable=height_variable, font=("Helvetica", 12), width=20)

        length_entry.place(rely=0.1, relx=0.5, anchor="center")
        width_entry.place(rely=0.3, relx=0.5, anchor="center")
        height_entry.place(rely=0.5, relx=0.5, anchor="center")

        # displaying the volume of cuboid
        display = ttk.Label(frame, text="")
        display.place(rely=0.7, relx=0.5, anchor="center")

        length_entry.bind("<Return>", volume_of_cuboid)
        width_entry.bind("<Return>", volume_of_cuboid)
        height_entry.bind("<Return>", volume_of_cuboid)

    elif shape == "Cylinder":
        def volume_of_cylinder(event):
            try:
                radius = radius_variable.get()
                height = height_variable.get()
                volume = round((pi * float(radius) ** 2) * float(height), 2)
                ttk.Label(frame, text=f"Volume:").place(rely=0.5, relx=0.25, anchor="center")
                display.config(text=f"{volume}")
            except ValueError:
                ttk.Label(frame, text=f"Volume:").place(rely=0.5, relx=0.25, anchor="center")
                display.config(text="Invalid input")

        ttk.Label(frame, text="Radius:").place(rely=0.1, relx=0.25, anchor="center")
        ttk.Label(frame, text="Height:").place(rely=0.3, relx=0.25, anchor="center")

        radius_variable = StringVar()
        height_variable = StringVar()

        radius_entry = ttk.Entry(frame, textvariable=radius_variable, font=("Helvetica", 12), width=20)
        height_entry = ttk.Entry(frame, textvariable=height_variable, font=("Helvetica", 12), width=20)

        radius_entry.place(rely=0.1, relx=0.5, anchor="center")
        height_entry.place(rely=0.3, relx=0.5, anchor="center")

        # displaying the volume of cylinder
        display = ttk.Label(frame, text="")
        display.place(rely=0.5, relx=0.5, anchor="center")

        radius_entry.bind("<Return>", volume_of_cylinder)
        height_entry.bind("<Return>", volume_of_cylinder)

    elif shape == "Cone":
        def volume_of_cone(event):
            try:
                radius = radius_variable.get()
                height = height_variable.get()
                volume = round((pi * float(radius) ** 2) * float(height) / 3, 2)
                ttk.Label(frame, text=f"Volume:").place(rely=0.5, relx=0.25, anchor="center")
                display.config(text=f"{volume}")
            except ValueError:
                ttk.Label(frame, text=f"Volume:").place(rely=0.5, relx=0.25, anchor="center")
                display.config(text="Invalid input")

        ttk.Label(frame, text="Radius:").place(rely=0.1, relx=0.25, anchor="center")
        ttk.Label(frame, text="Height:").place(rely=0.3, relx=0.25, anchor="center")

        radius_variable = StringVar()
        height_variable = StringVar()

        radius_entry = ttk.Entry(frame, textvariable=radius_variable, font=("Helvetica", 12), width=20)
        height_entry = ttk.Entry(frame, textvariable=height_variable, font=("Helvetica", 12), width=20)

        radius_entry.place(rely=0.1, relx=0.5, anchor="center")
        height_entry.place(rely=0.3, relx=0.5, anchor="center")

        # displaying the volume of cone
        display = ttk.Label(frame, text="")
        display.place(rely=0.5, relx=0.5, anchor="center")

        radius_entry.bind("<Return>", volume_of_cone)
        height_entry.bind("<Return>", volume_of_cone)

    elif shape == "Triangular Prism":
        def volume_of_triangular_prism(event):
            try:
                length = length_variable.get()
                base = base_variable.get()
                height = height_variable.get()
                volume = (float(base) * float(height) * float(length)) / 2
                ttk.Label(frame, text=f"Volume:").place(rely=0.7, relx=0.25, anchor="center")
                display.config(text=f"{volume}")
            except ValueError:
                ttk.Label(frame, text=f"Volume:").place(rely=0.7, relx=0.25, anchor="center")
                display.config(text="Invalid input")

        ttk.Label(frame, text="Length:").place(rely=0.1, relx=0.25, anchor="center")
        ttk.Label(frame, text="Base:").place(rely=0.3, relx=0.25, anchor="center")
        ttk.Label(frame, text="Height:").place(rely=0.5, relx=0.25, anchor="center")

        length_variable = StringVar()
        base_variable = StringVar()
        height_variable = StringVar()

        length_entry = ttk.Entry(frame, textvariable=length_variable, font=("Helvetica", 12), width=20)
        base_entry = ttk.Entry(frame, textvariable=base_variable, font=("Helvetica", 12), width=20)
        height_entry = ttk.Entry(frame, textvariable=height_variable, font=("Helvetica", 12), width=20)

        length_entry.place(rely=0.1, relx=0.5, anchor="center")
        base_entry.place(rely=0.3, relx=0.5, anchor="center")
        height_entry.place(rely=0.5, relx=0.5, anchor="center")

        # displaying the volume of triangular prism
        display = ttk.Label(frame, text="")
        display.place(rely=0.7, relx=0.5, anchor="center")

        length_entry.bind("<Return>", volume_of_triangular_prism)
        base_entry.bind("<Return>", volume_of_triangular_prism)
        height_entry.bind("<Return>", volume_of_triangular_prism)

    elif shape == "Triangular Pyramid":

        def volume_of_triangular_pyramid(event):
            try:
                base = base_variable.get()
                base_height = base_height_variable.get()
                height = height_variable.get()
                volume = round(((float(base) * float(base_height) / 2) * float(height)) / 3, 2)
                ttk.Label(frame, text=f"Volume:").place(rely=0.7, relx=0.25, anchor="center")
                display.config(text=f"{volume}")
            except ValueError:
                ttk.Label(frame, text=f"Volume:").place(rely=0.7, relx=0.25, anchor="center")
                display.config(text="Invalid input")

        ttk.Label(frame, text="Base:").place(rely=0.1, relx=0.25, anchor="center")
        ttk.Label(frame, text="Base height:").place(rely=0.3, relx=0.25, anchor="center")
        ttk.Label(frame, text="Height:").place(rely=0.5, relx=0.25, anchor="center")

        base_variable = StringVar()
        base_height_variable = StringVar()
        height_variable = StringVar()

        base_entry = ttk.Entry(frame, textvariable=base_variable, font=("Helvetica", 12), width=20)
        base_height_entry = ttk.Entry(frame, textvariable=base_height_variable, font=("Helvetica", 12), width=20)
        height_entry = ttk.Entry(frame, textvariable=height_variable, font=("Helvetica", 12), width=20)

        base_entry.place(rely=0.1, relx=0.5, anchor="center")
        base_height_entry.place(rely=0.3, relx=0.5, anchor="center")
        height_entry.place(rely=0.5, relx=0.5, anchor="center")

        # displaying the volume of triangular pyramid
        display = ttk.Label(frame, text="")
        display.place(rely=0.7, relx=0.5, anchor="center")

        base_entry.bind("<Return>", volume_of_triangular_pyramid)
        base_height_entry.bind("<Return>", volume_of_triangular_pyramid)
        height_entry.bind("<Return>", volume_of_triangular_pyramid)

    elif shape == "Pyramid":
        def volume_of_pyramid(event):
            try:
                base = base_variable.get()
                height = height_variable.get()
                volume = round((float(base) ** 2) * float(height) / 3, 2)
                ttk.Label(frame, text=f"Volume:").place(rely=0.5, relx=0.25, anchor="center")
                display.config(text=f"{volume}")
            except ValueError:
                ttk.Label(frame, text=f"Volume:").place(rely=0.5, relx=0.25, anchor="center")
                display.config(text="Invalid input")

        ttk.Label(frame, text="Base:").place(rely=0.1, relx=0.25, anchor="center")
        ttk.Label(frame, text="Height:").place(rely=0.3, relx=0.25, anchor="center")

        base_variable = StringVar()
        height_variable = StringVar()

        base_entry = ttk.Entry(frame, textvariable=base_variable, font=("Helvetica", 12), width=20)
        height_entry = ttk.Entry(frame, textvariable=height_variable, font=("Helvetica", 12), width=20)

        base_entry.place(rely=0.1, relx=0.5, anchor="center")
        height_entry.place(rely=0.3, relx=0.5, anchor="center")

        # displaying the volume of pyramid
        display = ttk.Label(frame, text="")
        display.place(rely=0.5, relx=0.5, anchor="center")

        base_entry.bind("<Return>", volume_of_pyramid)
        height_entry.bind("<Return>", volume_of_pyramid)

    elif shape == "Hemisphere":
        def volume_of_hemisphere(event):
            try:
                radius = radius_variable.get()
                volume = round((pi * float(radius) ** 3) * 2 / 3, 2)
                ttk.Label(frame, text=f"Volume:").place(rely=0.3, relx=0.25, anchor="center")
                display.config(text=f"{volume}")
            except ValueError:
                ttk.Label(frame, text=f"Volume:").place(rely=0.3, relx=0.25, anchor="center")
                display.config(text="Invalid input")

        ttk.Label(frame, text="Radius:").place(rely=0.1, relx=0.25, anchor="center")

        radius_variable = StringVar()
        radius_entry = ttk.Entry(frame, textvariable=radius_variable, font=("Helvetica", 12), width=20)
        radius_entry.place(rely=0.1, relx=0.5, anchor="center")

        # displaying the volume of hemisphere
        display = ttk.Label(frame, text="")
        display.place(rely=0.3, relx=0.5, anchor="center")

        radius_entry.bind("<Return>", volume_of_hemisphere)

    style = ttk.Style()
    style.configure("TLabel", font=("Helvetica", 12, "bold"))


def shape_widgets_area(frame, shape):
    for widget in frame.winfo_children():
        widget.destroy()

    if shape == "Circle":
        def area_of_circle(event):
            try:
                radius = radius_variable.get()
                area = round(pi * (float(radius) ** 2), 2)
                ttk.Label(frame, text="AREA:").place(rely=0.3, relx=0.25, anchor="center")
                display.config(text=f"{area}")
            except ValueError:
                ttk.Label(frame, text="AREA:").place(rely=0.3, relx=0.25, anchor="center")
                display.config(text="Invalid input")

        ttk.Label(frame, text="Radius:").place(rely=0.1, relx=0.25, anchor="center")

        radius_variable = StringVar()
        radius_entry = ttk.Entry(frame, textvariable=radius_variable, font=("Helvetica", 12), width=20)
        radius_entry.place(rely=0.1, relx=0.5, anchor="center")

        # displaying the area of circle
        display = ttk.Label(frame, text="")
        display.place(rely=0.3, relx=0.5, anchor="center")

        radius_entry.bind("<Return>", area_of_circle)

    if shape == "Square":
        def area_of_square(event):
            try:
                side = side_variable.get()
                area = float(side) ** 2
                ttk.Label(frame, text="AREA:").place(rely=0.3, relx=0.25, anchor="center")
                display.config(text=f"{area}")
            except ValueError:
                ttk.Label(frame, text="AREA:").place(rely=0.3, relx=0.25, anchor="center")
                display.config(text="Invalid input")

        ttk.Label(frame, text="Length:").place(rely=0.1, relx=0.25, anchor="center")

        side_variable = StringVar()
        side_entry = ttk.Entry(frame, textvariable=side_variable, font=("Helvetica", 12), width=20)
        side_entry.place(rely=0.1, relx=0.5, anchor="center")

        # displaying area of square
        display = ttk.Label(frame, text="")
        display.place(rely=0.3, relx=0.5, anchor="center")

        side_entry.bind("<Return>", area_of_square)

    if shape == "Triangle":
        def area_of_triangle(event):
            try:
                base = base_variable.get()
                height = height_variable.get()
                area = round((float(base) * float(height)) / 2, 2)
                ttk.Label(frame, text="AREA:").place(rely=0.5, relx=0.25, anchor="center")
                display.config(text=f"{area}")
            except ValueError:
                ttk.Label(frame, text="AREA:").place(rely=0.5, relx=0.25, anchor="center")
                display.config(text="Invalid input")

        ttk.Label(frame, text="Base:").place(rely=0.1, relx=0.25, anchor="center")
        ttk.Label(frame, text="Height:").place(rely=0.3, relx=0.25, anchor="center")

        base_variable = StringVar()
        height_variable = StringVar()

        base_entry = ttk.Entry(frame, textvariable=base_variable, font=("Helvetica", 12), width=20)
        height_entry = ttk.Entry(frame, textvariable=height_variable, font=("Helvetica", 12), width=20)

        base_entry.place(rely=0.1, relx=0.5, anchor="center")
        height_entry.place(rely=0.3, relx=0.5, anchor="center")

        # displaying area of triangle
        display = ttk.Label(frame, text="")
        display.place(rely=0.5, relx=0.5, anchor="center")

        base_entry.bind("<Return>", area_of_triangle)
        height_entry.bind("<Return>", area_of_triangle)

    if shape == "Rectangle":

        def area_of_rectangle(event):
            try:
                length = length_variable.get()
                width = width_variable.get()
                area = float(length) * float(width)
                ttk.Label(frame, text="AREA:").place(rely=0.5, relx=0.25, anchor="center")
                display.config(text=f"{area}")
            except ValueError:
                ttk.Label(frame, text="AREA:").place(rely=0.5, relx=0.25, anchor="center")
                display.config(text="Invalid input")

        ttk.Label(frame, text="Length:").place(rely=0.1, relx=0.25, anchor="center")
        ttk.Label(frame, text="Width:").place(rely=0.3, relx=0.25, anchor="center")

        length_variable = StringVar()
        width_variable = StringVar()

        length_entry = ttk.Entry(frame, textvariable=length_variable, font=("Helvetica", 12), width=20)
        width_entry = ttk.Entry(frame, textvariable=width_variable, font=("Helvetica", 12), width=20)

        length_entry.place(rely=0.1, relx=0.5, anchor="center")
        width_entry.place(rely=0.3, relx=0.5, anchor="center")

        # displaying area of rectangle
        display = ttk.Label(frame, text="")
        display.place(rely=0.5, relx=0.5, anchor="center")

        length_entry.bind("<Return>", area_of_rectangle)
        width_entry.bind("<Return>", area_of_rectangle)

    if shape == "Oval":
        def area_of_oval(event):
            try:
                major_r = major_r_variable.get()
                minor_r = minor_r_variable.get()
                area = round(pi * float(major_r) * float(minor_r), 2)
                ttk.Label(frame, text="AREA:").place(rely=0.5, relx=0.25, anchor="center")
                display.config(text=f"{area}")
            except ValueError:
                ttk.Label(frame, text="AREA:").place(rely=0.5, relx=0.25, anchor="center")
                display.config(text="Invalid input")

        ttk.Label(frame, text="Major Radius:").place(rely=0.1, relx=0.25, anchor="center")
        ttk.Label(frame, text="Minor Radius:").place(rely=0.3, relx=0.25, anchor="center")

        major_r_variable = StringVar()
        minor_r_variable = StringVar()

        major_r_entry = ttk.Entry(frame, textvariable=major_r_variable, font=("Helvetica", 12), width=20)
        minor_r_entry = ttk.Entry(frame, textvariable=minor_r_variable, font=("Helvetica", 12), width=20)

        major_r_entry.place(rely=0.1, relx=0.5, anchor="center")
        minor_r_entry.place(rely=0.3, relx=0.5, anchor="center")

        # displaying area of oval
        display = ttk.Label(frame, text="")
        display.place(rely=0.5, relx=0.5, anchor="center")

        major_r_entry.bind("<Return>", area_of_oval)
        minor_r_entry.bind("<Return>", area_of_oval)

    if shape == "Semicircle":
        def area_of_semicircle(event):
            try:
                radius = radiusvariable.get()
                area = round(pi * float(radius) ** 2 / 2, 2)
                ttk.Label(frame, text="AREA:").place(rely=0.3, relx=0.25, anchor="center")
                display.config(text=f"{area}")
            except ValueError:
                ttk.Label(frame, text="AREA:").place(rely=0.3, relx=0.25, anchor="center")
                display.config(text="Invalid input")

        ttk.Label(frame, text="Radius:").place(rely=0.1, relx=0.25, anchor="center")

        radiusvariable = StringVar()
        radius_entry = ttk.Entry(frame, textvariable=radiusvariable, font=("Helvetica", 12), width=20)
        radius_entry.place(rely=0.1, relx=0.5, anchor="center")

        # displaying the area of semicircle
        display = ttk.Label(frame, text="")
        display.place(rely=0.3, relx=0.5, anchor="center")

        radius_entry.bind("<Return>", area_of_semicircle)

    style = ttk.Style()
    style.configure("TLabel", font="Arial 12 bold")













































