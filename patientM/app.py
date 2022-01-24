import tkinter as tk
from tkinter import ttk

from patient import Patient


class Medicine(ttk.Frame):
    pass


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Patient Management System")
        patient_frame = Patient(self, padding=10)
        patient_frame.pack(expand=True, fill=tk.BOTH)


def main():
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
