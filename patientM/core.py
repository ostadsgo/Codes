from datetime import datetime
import database as db


class Patient:
    def __init__(self, **kw):
        self.kw = kw

    def register(self) -> int:
        patient_id = db.create(db.Patient, self.kw)
        return patient_id


class Medicine:
    def __init__(self, **kw):
        self.kw = kw

    def create(self):
        med_id = db.create(db.Medicine, self.kw)
        return med_id


# --------------------
# Helper functions.
# --------------------
def convert_to_date(cls, date_str):
    return datetime.strptime(date_str, "%Y/%m/%d")
