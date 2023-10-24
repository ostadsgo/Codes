import tkinter as tk
from tkinter import ttk


class MainFrame(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master)
        self.args = args
        self.kwargs = kwargs
        self.label = ttk.Label(self, text="Enter your name: ")
        self.label.pack()
        self.name_entry = ttk.Entry(self)
        self.name_entry.pack()
        button = ttk.Button(self, text="Click Me", command=self.say_hello)
        button.pack()
        ttk.Button(self, text="Close", command=master.destroy).pack()
        self.name_entry.bind("<Return>",  self.say_hello)

    def say_hello(self, event=None):
        self.label["text"] = f"Hello, {self.name_entry.get().title()}"
        self.name_entry.delete(0, tk.END)


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        mainframe = MainFrame(self)
        mainframe.pack()


class App:
    def __init__(self) -> None:
        self.root = MainWindow()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()
