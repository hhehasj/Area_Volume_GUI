from tkinter import *
from tkinter.ttk import *


def main():
    # START
    root = Tk()
    root.title("Trial")
    root.geometry("350x200")
    # BODY
    text = Label(root, text="Hello World")
    text.grid()
    # END
    root.mainloop()


if __name__ == '__main__':
    main()
