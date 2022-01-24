"""
    Register a patient and add medicine in one form!
"""

import tkinter as tk
from tkinter import ttk

import tkcalendar as tkcal

from database import Database, Table, TableName


class Patient(ttk.Frame):
    db = Database("patient.db")

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
        record = (
            self.name.get(),
            self.gender.get(),
            self.phone.get(),
            self.date_of_birth.get(),
            self.address.get(),
            self.email.get(),
            self.disease.get(),
        )
        return record

    def register(self):
        record = self.get_patient()
        # save record (a patient ) to the db
        if not self.db.is_table_exists(TableName.patient):
            self.db.create_table(Table.patient)

        # After make sure that the patient table exists
        if self.db.create_record(Table.insert_patient, record):
            print(f"Patient {self.name.get()} created!")
