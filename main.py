from tkinter import *
from tkinter.ttk import *
from scrollable_Frame import ScrollFrame


class Window:
    def __init__(self, parent):
        self.root = parent

        self.mainTabs = Notebook(self.root)

    def setUp(self):
        self.mainTabs.grid(column=0, row=0)


if __name__ == '__main__':
    root = Tk()

    window = Window(root)

    root.mainloop()
