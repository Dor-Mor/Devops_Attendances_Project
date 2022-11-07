#!/usr/bin/env python3
import os
import mysql.connector
from dotenv import load_dotenv
import pandas as pd
import attendance

load_dotenv()

myConnection = mysql.connector.connect(host=os.getenv('HOST_NAME'), user=os.getenv("USER_NAME_DB"),
                                       passwd=os.getenv("PASSWORD_DB"), db=os.getenv("DATABASE"))

cur = myConnection.cursor()


def add_new_table():
    # running attendance function
    attendance.fix_csv()
    # delete table if exists
    cur.execute("DROP TABLE IF EXISTS all_meetings")
    # creating table - 'all_meetings'
    cur.execute("CREATE TABLE all_meetings("
                "Name varchar(255),"
                "mins varchar(255),"
                "percentage varchar(255))")
    #           "PRIMARY KEY(Name))")

    # Import the CSV File into the DataFrame
    all_meetings_data = pd.read_csv(os.getenv('LOCAL_ALL_MEETINGS'), index_col=False, delimiter=',')
    all_meetings_data = all_meetings_data.apply(lambda x: x.astype(str).str.upper())
    all_meetings_data["percentage"] = all_meetings_data["percentage"].str.rstrip("%").astype("float") / 100
    all_meetings_data['Name'] = all_meetings_data['Name'].astype(pd.StringDtype())
    all_meetings_data['mins'] = all_meetings_data['mins'].astype(float)

    all_meetings_data = all_meetings_data.groupby(["Name"], as_index=False)[["mins", "percentage"]].sum()
    all_meetings_data['percentage'] = pd.Series(
        ["{0:.2f}%".format(val * 100) for val in all_meetings_data['percentage']],
        index=all_meetings_data.index)

    # loop through the data frame
    names = all_meetings_data['Name']
    mins_list = all_meetings_data['mins']
    pre = all_meetings_data['percentage']
    dict = {'Name': names, 'mins': mins_list, 'percentage': pre}
    df = pd.DataFrame(dict)
    for i, row in df.iterrows():
        # here %S means string values
        sql = "INSERT INTO all_meetings VALUES (%s,%s,%s)"
        cur.execute(sql, tuple(row))
    myConnection.commit()
    myConnection.close()


def return_all_table():
    cur.execute("SELECT * FROM all_meetings")
    mysql.connection.commit()
    return cur.fetchall()
