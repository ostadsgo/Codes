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


@pony.db_session
def add_patient(**patient):
    Patient(**patient)


def make_db(filename="patient.db"):
    # create database file
    db.bind(provider="sqlite", filename=filename, create_db=True)
    # Trun on debug mode; should be before generate_mapping
    pony.set_sql_debug(True)
    # create tables in the database
    db.generate_mapping(create_tables=True)


if __name__ == "__main__":
    make_db()

    # # Some test
    # add_patient(
    #     name="John Doe",
    #     gender="Male",
    #     phone="+1 (515) 765 1190",
    #     date_of_birth=datetime.date(1982, 11, 27),
    #     address="US, LA, John Hopkins St. N.49",
    #     email="johndoe@mail.com",
    #     disease="Covid 19",
    # )

    # add_patient(
    #     name="Kate Doe",
    #     gender="Female",
    #     phone="+1 (515) 918 7119",
    #     date_of_birth=datetime.date(1984, 7, 11),
    #     address="US, LA, John Hopkins St. N.49",
    #     email="katedoe@mail.com",
    #     disease="Covid 19",
    # )
