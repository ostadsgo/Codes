from datetime import datetime
import database as db


class Patient:
    def __init__(self, **kw):
        self.kw = kw

    def register(self) -> int:
        patient_id = db.create(db.Patient, self.kw)
        return patient_id

    @classmethod
    def convert_to_date(cls, date_str):
        return datetime.strptime(date_str, "%Y/%m/%d")
