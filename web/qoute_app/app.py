import csv

from flask import Flask, jsonify

app = Flask(__name__)


def read_csv(filename):
    with open(filename, "r") as csv_file:
        reader = csv.reader(csv_file)
        content = list(reader)
    return content


@app.get("/app/v1/contacts/")
def contacts():
    contacts = read_csv("contacts.csv")
    return jsonify(contacts)

if __name__ == "__main__":
    app.run(debug=True)
