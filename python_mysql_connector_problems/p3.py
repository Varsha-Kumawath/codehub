# 3. Create and Modify a Table (Easy-Medium)
#
# Description: Create a table employees with columns: id (INT, PRIMARY KEY, AUTO_INCREMENT), name (VARCHAR(255)),
# and salary (FLOAT). Then, modify the table by adding a new column department (VARCHAR(100)).
# Finally, verify the changes by fetching the table structure using SQL queries.

import mysql.connector

my_db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Varsha1057@#",
    database="mysqldemodb"
)

my_cursor=my_db.cursor()

try :
    my_cursor.execute("SHOW TABLES")
    table_exists = any(table_column == ("workers",) for table_column in my_cursor.fetchall())
    if table_exists:
        alter_query = "ALTER TABLE workers ADD COLUMN department VARCHAR(100)"
        my_cursor.execute(alter_query)
        print(f"Updated the Column Successfully ")

    else:
        query="CREATE TABLE workers (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255),salary DECIMAL(10,2))"
        my_cursor.execute(query)
        print(f"Created Successfully ")


except mysql.connector.Error as pe:
    print(pe)
    # my_cursor.execute("SHOW COLUMNS FROM workers")
    my_cursor.execute("DESC workers")   # DESC workers-is used to check table structure (column properties like data type, keys, and constraints).
    for x in my_cursor.fetchall():
        print(x)





