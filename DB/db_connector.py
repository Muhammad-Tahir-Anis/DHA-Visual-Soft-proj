"""
Created on Fri Feb 11 11:55:08 2022

In this file we have connection string of database to establish connection with database.
we have "insertData" and "showData" functions to insert and retrieve data from database respectively.

@author: muham
"""

import mysql.connector


# establishing connection to database hosted on local server
def connect_db():
    conn = mysql.connector.connect(user="root", password="Qwerty01!", host="127.0.0.1", database="vehicle_counting_dha")
    cursor = conn.cursor()
    return conn, cursor
