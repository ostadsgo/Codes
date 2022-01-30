import tkinter as tk
from tkinter import ttk

from ui import PatientForm


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # ---------------
        #    Menubar
        # ---------------
        self.option_add("*tearOff", False)
        menubar = tk.Menu(self)
        # Menu itmes
        menu_patient = tk.Menu(menubar)
        menu_help = tk.Menu(menubar)
        # menu items config
        menubar.add_cascade(menu=menu_patient, label="Patient")
        menubar.add_cascade(menu=menu_help, label="Help")
        # Patient sub menus (commands)
        menu_patient.add_command(label="Register Patient", command=self.patient_form)
        menu_patient.add_command(label="Search Patient", command=self.search_form)
        # Help sub menus (commands)
        menu_help.add_command(label="About")

        self["menu"] = menubar

    def patient_form(self):
        form = PatientForm(self)
        print(form)

    def search_form(self):
        pass


def main():
    app = App()
    app.title("Patient Management System")
    app.mainloop()


if __name__ == "__main__":
    main()
