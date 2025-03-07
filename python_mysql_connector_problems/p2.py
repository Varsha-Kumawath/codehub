 # 2. Create and Drop a Database (Easy)
#
# Description: Write a Python program that connects to MySQL,
# creates a database named test_db, verifies its creation, and
# then drops it. Ensure that errors are handled properly in case the database already exists or doesn't exist when trying to drop it.


import mysql.connector

my_db = mysql.connector.connect(
        host="localhost",
        user='root',
        password="Varsha1057@#")

my_cursor = my_db.cursor()

# my_cursor.execute("SHOW DATABASES")
# for db in my_cursor.fetchall():
#     print(db) To check the whether it is Tuple or not if it tuple that it will end with , for each item


try:
    print("Connection Successful")
    my_cursor.execute("SHOW DATABASES")

    test_db_exists= any(db==("test_db",) for db in my_cursor.fetchall() )
    print(db==("test_db",) for db in my_cursor.fetchall() )

    if test_db_exists:
            print(f" Already Exists!")
            my_cursor.execute("DROP DATABASE test_db")
            print(f"Successfully Deleted")

    else:
        my_cursor.execute("CREATE DATABASE test_db")
        print(f"Created Successfully ")

except mysql.connector.Error as pe:
    print(f"Connection Failed with Error= {pe}")