from tkinter import *
from tkinter import ttk
from Area_window import *
from Volume_window import *


def main():
    # START
    root = Tk()
    root.title("Trial")

    # WINDOW DIMENTSIONS
    screen_width = root.winfo_screenwidth()  # Gets width of the screen
    screen_height = root.winfo_screenheight()  # Gets height of the screen

    # Gets the center point
    center_x = int(screen_width/2 - 1000/2)
    center_y = int(screen_height/2 - 500/2)

    root.geometry(f"600x350+{center_x}+{center_y}")

    # BODY
    text1 = Label(root, text="CHOOSE:", font=("Arial", 25))
    text1.place(x=300, y=25, anchor=CENTER)

    area_button = ttk.Button(root, text="AREA", width=10, command=Area_Window)
    area_button.place(x=150, y=150, anchor=CENTER)

    volume_button = ttk.Button(root, text="VOLUME", width=10, command=Volume_Window)
    volume_button.place(x=450, y=150, anchor=CENTER)
    # END
    root.mainloop()


if __name__ == '__main__':
    main()
