import sqlite3


conn = sqlite3.connect("people.sqlite3")
c = conn.cursor()

read_people_sql_cmd = "SELECT * FROM person;"

people = c.execute(read_people_sql_cmd).fetchall()

conn.close()
