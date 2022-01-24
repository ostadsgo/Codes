# create a method to check if a table exists or not;

import sqlite3 as sqlite


class TableName:
    patient = "patient"
    medicine = "medicieeruuund''/e"


class Table:
    patient = """ CREATE TABLE IF NOT EXISTS "patient" (
                        "id" INTEGER NOT NULL PRIMARY KEY UNIQUE,
                        "name"	TEXT,
                        "gender" TEXT,
                        "phone"	TEXT,
                        "date_of_birth"	TEXT,
                        "address"	TEXT,
                        "email"	TEXT,
                        "disease"	TEXT
                    );
                """
    table_exists = """
        SELECT name 
        FROM sqlite_master 
        WHERE type='table' 
        AND name = ?;
    """

    insert_patient = sql = """ INSERT INTO patient (
                name,
                gender,
                phone,
                date_of_birth,
                address,
                email,
                disease
            ) 
    VALUES(?, ?, ?, ?, ?, ?, ?);
    """


class Database:
    def __init__(self, db_name):
        self.db_name = db_name

    def connect(self):
        try:
            conn = sqlite.connect(self.db_name)
            return conn
        except sqlite.Error as e:
            print(e)

    def create_table(self, sql):
        conn = self.connect()
        with conn:
            cursor = conn.cursor()
            cursor.execute(sql)

    def is_table_exists(self, tbl_name):
        conn = self.connect()
        tbl = Table()
        with conn:
            cursor = conn.cursor()
            cursor.execute(tbl.table_exists, (tbl_name,))
            return cursor.fetchone()

    def create_record(self, sql, record):
        conn = self.connect()
        with conn:
            cursor = conn.cursor()
            cursor.execute(sql, record)
            return True
        return False


if __name__ == "__main__":
    # create patient table
    table = Table()
    patient_table_sql = table.patient
    db = Database("patient.db")
    db.create_table(patient_table_sql)
    res = db.is_table_exists("patient")
    print(res)
