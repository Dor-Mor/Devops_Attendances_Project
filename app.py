#!/usr/bin/env python3
import database
from flask import Flask

app = Flask(__name__)


#@app.before_first_request
#def before_first_request():
#    database.add_new_table()


@app.route('/')
def hello():
    return 'Attendance project'


if __name__ == 'main':
    app.run(host='localhost', port=5000)
