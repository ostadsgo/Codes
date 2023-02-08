import sqlite3


def create_student_table():
    conn = sqlite3.connect("student.db")

    sql = """
        CREATE TABLE IF NOT EXISTS student (
            id integer primary key,
            name text,
            age integer,
            grade real
        );
    """

    cur = conn.cursor()
    cur.execute(sql)
    conn.close()
    print("table student created!")

def all_student():
    conn = sqlite3.connect("student.db")
    sql = "SELECT * FROM student"
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    print(rows)

def student_a(grade=18):
    conn = sqlite3.connect("student.db")
    sql = "SELECT * FROM student WHERE grade >= ?"
    cur = conn.cursor()
    cur.execute(sql, (grade,))
    rows = cur.fetchall()
    print(rows)

def create_student():
    conn = sqlite3.connect("student.db")
    sql = """
        INSERT INTO student
        VALUES (?, ?, ?)
    """
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    grade = input("Enter your grade: ")

    cur = conn.cursor()
    cur.execute(sql, (name, age, grade))
    conn.commit()
    print(f"student {name} {age} {grade} inserted.")
    conn.close()

create_student()
