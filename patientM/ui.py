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


class PatientFrame(ttk.Frame):
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
        self.gender.set("Female")
        self.gender.pack()

        # row 2
        ttk.Label(self, text="Phone ").pack()
        self.phone = ttk.Entry(self)
        self.phone.pack()

        # row 3
        ttk.Label(self, text="Date of Bright").pack()
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

        for child in self.winfo_children():
            child.pack_configure(fill=tk.BOTH, expand=True)
            if child.widgetName == "ttk::label":
                child.pack_configure(pady=(20, 0))

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


class MedicineFrame(ttk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.timeslot_num = 3
        self.row_num = 5
        self.rows = []
        self.ui()

    def _header(self):
        frame = ttk.Frame(self, relief="sunken", padding=(5, 5))
        frame.pack(fill=tk.X)
        titles = {"Medicine": 160, "Timeslot 1": 20, "Timeslot 2": 20, "Timeslot3": 20}
        for title, pad in titles.items():
            ttk.Label(frame, text=title).pack(side=tk.LEFT, fill=tk.X, padx=(0, pad))

    def _medicine_table(self, row_num=5):
        # size of entries. 30 for medicine 10 for timeslots
        col_sizes = (30,) + (10,) * self.timeslot_num
        for _ in range(row_num):
            frame = ttk.Frame(self, padding=(5, 3))
            frame.pack(fill=tk.X)
            row = []
            for size in col_sizes:
                e = ttk.Entry(frame, width=size)
                e.pack(side=tk.LEFT, fill=tk.X, padx=(0, 5))
                self.rows.append(e)

    def ui(self):
        self._header()
        self._medicine_table()


class PatientForm(tk.Toplevel):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        # Patient register frame
        pati_frame = PatientFrame(self)
        pati_frame.pack(side=tk.LEFT)

        # Medicine table frame
        style = ttk.Style(self)
        style.configure("medicine.TFrame", background="#457B9D")
        med_frame = MedicineFrame(self, style="medicine.TFrame")
        med_frame.pack()

        ttk.Button(self, text="Submit", command=self.on_submit).pack()

    def on_submit(self):
        print("on submit pressed!")
