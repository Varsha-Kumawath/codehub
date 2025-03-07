# 4. Insert Multiple Records into a Table (Medium)
#
# Description: Write a Python script that inserts multiple employee records into the employees
# table using executemany(). Ensure that the script can insert at least 5 records in one go.

import mysql.connector

my_db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Varsha1057@#",
    database="mysqldemodb"
)

my_cursor=my_db.cursor()

query="INSERT INTO workers (name,salary,department) values (%s,%s,%s) "
values=[
    ("varsha",35000,"INFRA"),
    ("Jazz",80000,"APPS"),
    ("Vijay", 150000,"NETWORK"),
    ("Mani",750000,"CYBER SECURITY"),
    ("Sandya", 27000,"SERVICE DESK")
]
my_cursor.executemany(query,values)
my_db.commit()
my_cursor.execute("select * from workers")

for x in my_cursor.fetchall():
    print(x)