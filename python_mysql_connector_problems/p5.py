# 5. Retrieve and Display Data (Medium)
#
# Description: Write a Python script to retrieve all records from the employees table
# and display them in a formatted output. Implement error handling to catch connection or execution errors.

import mysql.connector
from tabulate import tabulate   # Installed tabulate to display the records


my_db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Varsha1057@#",
    database="mysqldemodb"
)

db_cursor=my_db.cursor()

try:
    query="SELECT * FROM workers"
    db_cursor.execute(query)

    results=db_cursor.fetchall()
    if results:
        print("\n Workers Table Data:\n")
        column_names = [desc[0] for desc in db_cursor.description]
        print(tabulate(results, headers=column_names, tablefmt="grid"))
    else:
        print("No Records found")

except mysql.connector.errors as e:
    print(e)