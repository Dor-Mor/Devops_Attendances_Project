#!/usr/bin/env python3
import database
import attendance
from flask import Flask

app = Flask(__name__)


@app.before_first_request
def before_first_request():
    attendance.fix_csv()
    database.add_new_table()


@app.route('/')
def hello():
    return 'Attendance project'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
