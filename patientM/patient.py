"""
    Register a patient and add medicine in one form!
"""
from datetime import datetime
import email
import tkinter as tk
from tkinter import ttk

import tkcalendar as tkcal

from database import create, Patient


# class Test:
#     name: str
#     age: int


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
        ttk.Button(self, text="Submit", command=self.register).pack()

        # config all widgets
        for child in self.winfo_children():
            child.pack_configure(fill=tk.BOTH, expand=True)
            if child.widgetName == "ttk::label":
                child.pack_configure(pady=(10, 0))

    # Get patient data from registration form.
    def get_patient(self):
        patient = dict(
            name=self.name.get(),
            gender=self.gender.get(),
            phone=self.phone.get(),
            date_of_birth=datetime.now().date(),
            address=self.address.get(),
            email=self.email.get(),
            disease=self.disease.get(),
        )
        return patient

    def register(self):
        patient = self.get_patient()
        patient_id = create(Patient, patient)
