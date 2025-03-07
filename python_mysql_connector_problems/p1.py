# 1. Connect to MySQL Database (Easy)s
#
# Description: Write a Python script to connect to a MySQL database using mysql.connector.
# The program should take the host, user, and password as input, connect to the database, and
# print "Connected successfully" if the connection is successful.
# Otherwise, handle the error and display an appropriate message.

import mysql.connector
try:
    my_db = mysql.connector.connect(
        host="localhost",
        user='root',
        password="Varsha10@#",
        database="mysqldemodb"
    )
    print(my_db)
    print("Connection Successful")
except mysql.connector.Error as pe:
    print(f"Connection Failed with Error= {pe}")