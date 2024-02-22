import tkinter as tk
from tkinter import ttk


class Menu(ttk.Frame):
    def __init__(self, master):
        pass


class TextBox(ttk.Frame):
    def __init__(self, master):
        pass


class App(tk.Tk):
    def __init__(self):
        super().__init__()

    def run(self):
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()
