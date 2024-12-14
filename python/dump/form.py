import tkinter as tk
from tkinter import ttk


class Form(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.ui()

    def ui(self):
        # Labels
        ttk.Label(self, text="First Name"). grid(row=0, column=0)
        ttk.Label(self, text="Last Name").grid(row=1, column=0)
        # Entry
        first_name = ttk.Entry(self)
        last_name = ttk.Entry(self)
        first_name.grid(row=0, column=1)
        last_name.grid(row=1, column=1)
        # button
        ttk.Button(self, text="Save").grid(row=2, column=0)
        ttk.Button(self, text="Cancel").grid(row=2, column=1)


class MainFrame(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        form = Form(master)
        form.pack(expand=True, fill="both")


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("From App")
        mainframe = MainFrame(self)
        mainframe.pack(expand=True, fill="both")

    def run(self):
        self.mainloop()


def main():
    app = App()
    app.run()


if __name__ == "__main__":
    main()

