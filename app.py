#!/usr/bin/env python3
import database
import attendance
import download_csv
from flask import Flask, render_template

app = Flask(__name__, template_folder=".")


@app.before_first_request
def before_first_request():
    download_csv.download_csv()
    attendance.fix_csv()
    database.add_new_table()


@app.route('/')
def main_route():
    students = database.return_all_table()
    return render_template('index.html', students=students)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
