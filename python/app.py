import database as db

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


# Helper functions
def clear_entry(frame):
    for child in frame.children.values():
        if child.widgetName == "ttk::entry":
            child.delete(0, "end")


def search(name):
    name = name.lower().strip()
    patients = db.search_by_patient_name(name)
    print(patients)
    return patients


def create_medicine(med_frame, patient_id):
    # Get prescription values
    rows = []
    for row_frame in list(med_frame.children.values())[1:]:  # [1: ] skip header
        row = []
        for child in row_frame.children.values():
            row.append(child.get().lower())
        rows.append(row)

    prescription = {
        index: {"medicine": row[0], "timeslots": row[1:]}
        for index, row in enumerate(rows)
        if row[0]
    }

    # Database opertion
    medicine_ids_timeslots = {}
    for item in prescription.values():
        # Get medicine name
        medicine = item.get("medicine")
        # insert medicine to the table
        medicine_id = db.insert_medicine([patient_id, medicine])
        # extract valid timeslot; skip the empty timeslots.
        timeslots = [value for value in item.get("timeslots") if value]
        # create the dict with med id and timeslots for it.
        medicine_ids_timeslots[medicine_id] = timeslots

    # Save timeslots
    for medicine_id, timeslots in medicine_ids_timeslots.items():
        for timeslot in timeslots:
            db.insert_timeslot([medicine_id, timeslot])

    # clear all entries values.
    for row_frame in list(med_frame.children.values())[1:]:
        clear_entry(row_frame)


def create_patient(patient_frame):
    patient = []
    for child in patient_frame.children.values():
        if child.widgetName == "ttk::entry":
            patient.append(child.get().lower())

    if patient[-2] in db.get_emails():
        err_title = "Email Exists Error"
        err_msg = "The email already exists in the patient table."
        messagebox.showerror(err_title, err_msg)
        return

    # Insert patient to the db
    patiend_id = db.insert_patient(patient)

    # clear entries after db operation.
    clear_entry(patient_frame)

    return patiend_id


def submit(patient_frame, med_frame):
    patient_id = create_patient(patient_frame)
    if patient_id is not None:
        create_medicine(med_frame, patient_id)


def patient_ui(patient_frame):
    # row 0
    ttk.Label(patient_frame, text="Name: ").grid(row=0, column=0)
    name = ttk.Entry(patient_frame)
    name.grid(row=0, column=1)

    # row 1
    ttk.Label(patient_frame, text="Gender: ").grid(row=1, column=0)
    gender = ttk.Entry(patient_frame)
    gender.grid(row=1, column=1)

    # row 2
    ttk.Label(patient_frame, text="Phone: ").grid(row=2, column=0)
    phone = ttk.Entry(patient_frame)
    phone.grid(row=2, column=1)

    # row 3
    ttk.Label(patient_frame, text="Date of Bright: ").grid(row=3, column=0)
    date_of_birth = ttk.Entry(patient_frame)
    date_of_birth.grid(row=3, column=1)

    # row 4
    ttk.Label(patient_frame, text="Address: ").grid(row=4, column=0)
    address = ttk.Entry(patient_frame)
    address.grid(row=4, column=1)

    # row 5
    ttk.Label(patient_frame, text="Email: ").grid(row=5, column=0)
    email = ttk.Entry(patient_frame)
    email.grid(row=5, column=1)

    # row 6
    ttk.Label(patient_frame, text="Disease: ").grid(row=6, column=0)
    disease = ttk.Entry(patient_frame)
    disease.grid(row=6, column=1)

    # config all widgets
    for child in patient_frame.winfo_children():
        child.grid_configure(pady=10, padx=10)


def med_ui(med_frame):
    # ---------------------
    #     Medicine Talbe
    # ---------------------
    # header of the table
    header_titles = ("Medicine", "Timeslot 1", "Timeslot 2", "Timeslot 3")
    header_frame = ttk.Frame(med_frame, padding=5, relief="sunken")
    header_frame.pack()
    for title in header_titles:
        ttk.Label(header_frame, text=title).pack(padx=5, pady=5, side="left")

    # rows of the table
    field_num = len(header_titles)
    row_num = 10
    row_frames = []

    for _ in range(row_num):
        row_frame = ttk.Frame(med_frame, padding=5)
        row_frame.pack()
        row_frames.append(row_frame)
        for col_num in range(field_num):
            if col_num == 0:
                ttk.Entry(row_frame, width=20).pack(side="left", padx=5, pady=5)
            else:
                ttk.Entry(row_frame, width=10).pack(side="left", padx=5, pady=5)


def search_result_ui(name_entry, patient_var):
    patients = []
    # Search result
    name = name_entry.get()
    search_result = search(name)
    patients = [f"{record[1]} | {record[-2]}" for record in search_result]
    patient_var.set(patients)


def test(event):
    print("something")


def search_ui(search_frame):
    # tk Variables
    patients_var = tk.StringVar()

    # Search
    search_area_frame = ttk.Frame(search_frame, padding=5)
    search_area_frame.pack()
    ttk.Label(search_area_frame, text="Name: ").pack(side="left")
    patient_name = ttk.Entry(search_area_frame)
    patient_name.pack(side="left", padx=10)
    search_button = ttk.Button(search_area_frame, text="Search")
    search_button.pack()
    search_button["command"] = lambda: search_result_ui(
        patient_name,
        patients_var,
    )

    # Search result part
    search_result_frame = ttk.Frame(search_frame, padding=5)
    search_result_frame.pack(expand=True, fill="x")
    ttk.Label(search_result_frame, text="Search Result").grid(
        row=0, column=0, sticky="w"
    )

    # patient Listbox
    patient_listbox = tk.Listbox(search_result_frame, listvariable=patients_var)
    patient_listbox.grid(row=1, column=0, sticky="w")
    patient_listbox.bind("<<ListboxSelect>>", lambda e: test(e))


def register_patient_form(root):
    # Toplevel window
    patient_form = tk.Toplevel(root)
    patient_form.title("Register Patient")

    # Patient UI
    patient_frame = ttk.Frame(patient_form, relief="sunken", padding=(10, 30))
    patient_frame.pack(side="left")
    patient_ui(patient_frame)

    # Medicen UI
    med_frame = ttk.Frame(patient_form, padding=(5, 10), relief="groove")
    med_frame.pack()
    med_ui(med_frame)

    # submit button for register a patient
    submit_button = ttk.Button(patient_form, text="Submit")
    submit_button["command"] = lambda: submit(patient_frame, med_frame)
    submit_button.pack()


def search_patient_form(root):
    # Search top level window
    search_form = tk.Toplevel(root)
    search_form.title("Search Patient")

    # Search UI
    search_frame = ttk.Frame(search_form, padding=5)
    search_frame.pack()
    search_ui(search_frame)


def main():
    # GUI
    root = tk.Tk()
    root.geometry("700x500")
    # ---------------
    #    Menubar
    # ---------------
    root.option_add("*tearOff", False)
    menubar = tk.Menu(root)
    # Menu itmes
    menu_patient = tk.Menu(menubar)
    menu_help = tk.Menu(menubar)
    # menu items config
    menubar.add_cascade(menu=menu_patient, label="Patient")
    menubar.add_cascade(menu=menu_help, label="Help")
    # Patient sub menus (commands)
    menu_patient.add_command(
        label="Register Patient",
        command=lambda: register_patient_form(root),
    )
    menu_patient.add_command(
        label="Search Patient",
        command=lambda: search_patient_form(root),
    )
    # Help sub menus (commands)
    menu_help.add_command(label="About")

    root["menu"] = menubar

    root.mainloop()


if __name__ == "__main__":
    main()
