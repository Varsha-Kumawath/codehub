# 8. Transaction Handling (Hard)
#
# Description: Write a Python script that performs two queries inside a transaction:
#
# Insert a new employee.
#
# Update the salary of another employee.
# If any operation fails, roll back the transaction; otherwise, commit the changes.

import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Varsha1057@#",
    database="mysqldemodb"
)

db_cursor =db.cursor()

new_emp_name=input("> Create New Employee name: ")
new_emp_salary=float(input("> Create New Employee salary: "))
new_emp_dep=input("> Create New Employee department: ")

try:

    db.start_transaction()  #Used db.start_transaction() — Ensures rollback on failure.

    db_cursor.execute("SELECT * from workers where name=%s",(new_emp_name,))
    emp_exists=db_cursor.fetchone()

    if emp_exists:
        print(f"Emp Record already exists")

        emp_id=input(">Enter emp id that you want to update salary for ")
        up_emp_salary =float(input(f"> Kindly Update New salary to employee id {emp_id}: " ))

        update_query="Update workers SET salary= %s where id = %s"
        db_cursor.execute(update_query,(up_emp_salary,emp_id))

        print(f"Employee - {emp_id} updated with new salary {up_emp_salary}")
    else:
        create_query="INSERT INTO workers (name,salary,department) values(%s,%s,%s) "
        db_cursor.execute(create_query,(new_emp_name,new_emp_salary,new_emp_dep))

        print(f"New Employee id : {db_cursor.lastrowid} and name : {new_emp_name} , created with salary - {new_emp_salary} rupees and aligned to {new_emp_dep} department successfully")
    db.commit()

except mysql.connector.Error as e:
    print(f"Transaction Failed !,Rolling back. Error:{e}")
    db.rollback()