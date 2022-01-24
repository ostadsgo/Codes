# built-in imports
import datetime

# pony - 3rd party
import pony.orm as pony


db = pony.Database()


class Patient(db.Entity):
    name = pony.Required(str)
    gender = pony.Required(str)
    phone = pony.Required(str)
    date_of_birth = pony.Required(datetime.date)
    address = pony.Required(str)
    email = pony.Required(str)
    disease = pony.Required(str)
    prescriptions = pony.Set("Prescription")


class Prescription(db.Entity):
    date = pony.Required(datetime.date)
    person = pony.Required(Patient)
    medicines = pony.Set("Medicine")


class Medicine(db.Entity):
    name = pony.Required(str)
    prescription = pony.Required(Prescription)
    timeslots = pony.Set("Timeslot")


class Timeslot(db.Entity):
    time = pony.Required(datetime.time)
    medicine = pony.Required(Medicine)


def run():
    # create database file
    db.bind(provider="sqlite", filename="patient.db", create_db=True)
    # create tables in the database
    db.generate_mapping(create_tables=True)


if __name__ == "__main__":
    run()
