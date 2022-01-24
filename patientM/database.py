# built-in imports
import datetime

# pony - 3rd party
import pony.orm as pony


FILENAME = "patient.db"
db = pony.Database()


class Patient(db.Entity):
    name = pony.Required(str)
    gender = pony.Required(str)
    phone = pony.Required(str)
    date_of_birth = pony.Required(datetime.date)
    address = pony.Required(str)
    email = pony.Required(str, unique=True)
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
def create(entity, record):
    o = entity(**record)
    return o.id


db.bind(provider="sqlite", filename=FILENAME, create_db=True)
db.generate_mapping(create_tables=True)


def make_db(filename="patient.db"):
    # create database file
    db.bind(provider="sqlite", filename=filename, create_db=True)
    # Trun on debug mode; should be before generate_mapping
    # pony.set_sql_debug(True)
    # create tables in the database
    db.generate_mapping(create_tables=True)


if __name__ == "__main__":
    # make_db()
    idx = create("x, ", "y")
    print(idx)
