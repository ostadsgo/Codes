"""
Create a simple tkinter program.
"""
import tkinter as tk
from tkinter import ttk


# This class is a class inhereted from `mainframe`
class MainFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

    def ui(self):
        label = ttk.Label(self, text="Hello World!")
        label.grid(row=0, column=0)


def main():
    root = tk.Tk()
    mainframe = MainFrame(root)
    mainframe.pack(fill=tk.BOTH, expand=True)
    root.mainloop()


if __name__ == "__main__":
    main()
