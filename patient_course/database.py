import sqlite3 as sqlite


def create_patient_table():
    conn = sqlite.connect("patient.db")
    cur = conn.cursor()

    sql = """ CREATE TABLE IF NOT EXISTS "patient" (
        "id"	INTEGER NOT NULL UNIQUE,
        "name"	TEXT,
        "gender" TEXT,
        "phone"	TEXT,
        "date_of_birth"	TEXT,
        "address"	TEXT,
        "email"	TEXT,
        "disease"	TEXT,
        PRIMARY KEY("id" AUTOINCREMENT)
    );
    """
    cur.execute(sql)
    conn.close()


def insert_patient(record):
    conn = sqlite.connect("patient.db")
    cur = conn.cursor()

    sql = """ INSERT INTO patient (
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
    cur.execute(sql, record)
    conn.commit()  # save data in the table
    print(f"Patient inserted with the id of {cur.lastrowid}!")
    return cur.lastrowid
    conn.close()


def get_emails():
    conn = sqlite.connect("patient.db")
    cur = conn.cursor()
    sql = "SELECT email FROM patient;"
    cur.execute(sql)
    emails = cur.fetchall()
    emails = [email[0] for email in emails]
    conn.close()
    return emails


def create_medicine_table():
    conn = sqlite.connect("patient.db")
    cur = conn.cursor()
    sql = """ CREATE TABLE IF NOT EXISTS medicine (
              id INTEGER NOT NULL UNIQUE,
              patient_id INTEGER NOT NULL,
              name TEXT,
              PRIMARY KEY ("id" AUTOINCREMENT),
              FOREIGN KEY (patient_id) REFERENCES patient (id)
    )
    
    """
    cur.execute(sql)
    conn.close()


def create_timeslot_table():
    conn = sqlite.connect("patient.db")
    cur = conn.cursor()
    sql = """ CREATE TABLE IF NOT EXISTS timeslot (
              id INTEGER NOT NULL UNIQUE,
              medicine_id INTEGER NOT NULL,
              time TEXT,
              PRIMARY KEY ("id" AUTOINCREMENT),
              FOREIGN KEY (medicine_id) REFERENCES medicine (id)
    )
    
    """
    cur.execute(sql)
    conn.close()


def insert_medicine(record):
    conn = sqlite.connect("patient.db")
    cur = conn.cursor()

    sql = """ INSERT INTO medicine (
                    patient_id, name
              ) 
              VALUES(?, ?);
    """
    cur.execute(sql, record)
    conn.commit()  # save data in the table
    print(f"Medicine inserted succussfuly.")
    return cur.lastrowid
    conn.close()


def insert_timeslot(record):
    conn = sqlite.connect("patient.db")
    cur = conn.cursor()

    sql = """ INSERT INTO timeslot (
                    medicine_id, time
              ) 
              VALUES(?, ?);
    """
    cur.execute(sql, record)
    conn.commit()  # save data in the table
    print(f"Timeslot inserted succussfuly.")
    conn.close()


def search_by_patient_name(name):
    conn = sqlite.connect("patient.db")
    cur = conn.cursor()
    sql = "SELECT * FROM patient WHERE name=?"
    cur.execute(sql, (name,))
    patients = cur.fetchall()
    conn.close()
    return patients


if __name__ == "__main__":
    # TEST AREA
    # -------------------
    # create patient table
    # create_patient_table()

    # patient1 = ("Keven", "M", "2342432", "2021", "US", "j@m.com", "Cancer Blood")
    # insert_patient(patient1)
    # print("data inserted!")
    # create_medicine_table()
    # create_timeslot_table()
    timeslots = [("4", "8:00"), ("4", "20:00")]
    for timeslot in timeslots:
        insert_timeslot(timeslot)
