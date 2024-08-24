import tkinter
from tkinter import *
from tkinter import ttk
from Area_window import *
from Volume_window import *


def hide_window(self):
    self.withdraw()


def main():
    def konami_code(event):
        # BEAR IMAGE
        bear_jpg = Image.open("./icons_and_photo/bear.jpg")
        bear_image = ImageTk.PhotoImage(bear_jpg)
        root.bear_image = bear_image

        # IMAGE is displayed
        image_label = Label(root, image=bear_image)
        image_label.place(x=300, y=175, anchor=CENTER)

    root = Tk()
    # When you press the keys, it will show a label
    root.bind("<Up><Up><Down><Down><Left><Right><Left><Right><KeyPress-b><KeyPress-a>", konami_code)

    # START
    root.title("Trial")
    root.resizable(False, False)
    screen_width = root.winfo_screenwidth()  # Gets width of the screen

    # WINDOW DIMENTSIONS
    # Gets height of the screen

    screen_height = root.winfo_screenheight()  # Gets the center point
    center_x = int(screen_width / 2 - 600 / 2)
    center_y = int(screen_height / 2 - 350 / 2)
    root.geometry(f"600x350+{center_x}+{center_y}")

    text1 = ttk.Label(root, text="CHOOSE:", font=("Arial", 25))

    # BODY
    text1.place(x=300, y=25, anchor=CENTER)
    area_button = ttk.Button(root, text="AREA", width=10,
                             command=lambda: [Area_Window(main_window=root), hide_window(root)])

    area_button.place(x=150, y=150, anchor=CENTER, width=75, height=50)
    volume_button = ttk.Button(root, text="VOLUME", width=10,
                               command=lambda: [Volume_Window(main_window=root), hide_window(root)])

    volume_button.place(x=450, y=150, anchor=CENTER, width=75, height=50)

    # END
    root.mainloop()


if __name__ == '__main__':
    main()
