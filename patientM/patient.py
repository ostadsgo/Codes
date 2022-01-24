"""
    Register a patient and add medicine in one form!
"""

import tkinter as tk

from datetime import datetime
from tkinter import ttk

# 3rd
import tkcalendar as tkcal

# self
import core


class PatientForm(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.ui()

    def ui(self):
        # row 0
        ttk.Label(self, text="Patient Name ").pack()
        self.name = ttk.Entry(self)
        self.name.pack()

        # row 1
        ttk.Label(self, text="Gender ").pack()
        self.gender = ttk.Combobox(self, values=["Female", "Male", "Other"])
        self.gender.pack()

        # row 2
        ttk.Label(self, text="Phone ").pack()
        self.phone = ttk.Entry(self)
        self.phone.pack()

        # row 3
        ttk.Label(self, text="Date of Bright (yyyy/mm/dd)").pack()
        self.date_of_birth = tkcal.DateEntry(
            self,
            width=12,
            background="darkblue",
            foreground="white",
            borderwidth=2,
            date_pattern="yyyy/mm/dd",
        )
        self.date_of_birth.pack()

        # row 4
        ttk.Label(self, text="Address (City/Stree)").pack()
        self.address = ttk.Entry(self)
        self.address.pack()

        # row 5
        ttk.Label(self, text="Email Address").pack()
        self.email = ttk.Entry(self)
        self.email.pack()

        # row 6
        ttk.Label(self, text="Disease Name").pack()
        self.disease = ttk.Entry(self)
        self.disease.pack()

        # row 7 - submit button
        ttk.Button(self, text="Submit", command=self.on_submit).pack()

        # config all widgets
        for child in self.winfo_children():
            child.pack_configure(fill=tk.BOTH, expand=True)
            if child.widgetName == "ttk::label":
                child.pack_configure(pady=(10, 0))

    # Clear form entry fields
    def clear_fields(self):
        for child in self.winfo_children():
            if child.widgetName == "ttk::entry":
                child.delete(0, tk.END)

    # Get patient data from registration form.
    def get_patient(self):
        patient = core.Patient(
            name=self.name.get(),
            gender=self.gender.get(),
            phone=self.phone.get(),
            date_of_birth=core.Patient.convert_to_date(self.date_of_birth.get()),
            address=self.address.get(),
            email=self.email.get(),
            disease=self.disease.get(),
        )
        return patient

    def on_submit(self):
        patient = self.get_patient()
        patient.register()
        self.clear_fields()
        print("The patient registerd")
