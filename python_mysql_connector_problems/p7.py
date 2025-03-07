# 7. Update and Delete Records (Medium-Hard)
#
# Description: Write a Python script that updates the salary of an employee based on their ID.
# Then, implement a function that deletes an employee record based on the ID. Ensure that changes are reflected in the database

import mysql.connector

my_db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Varsha1057@#",
    database="mysqldemodb"
)

db_cursor=my_db.cursor()

# Function to Update Salary
u_emp_id=input(">Enter your Emp Id: ")
u_salary=input("> Enter the salary you want to update: ")


def update_salary(u_salary, u_emp_id):
    update_query="Update workers set salary = %s Where id = %s"
    db_cursor.execute(update_query,(u_salary,u_emp_id))
    my_db.commit()
    db_cursor.execute("Select * from workers where id= %s", (u_emp_id,))
    result=db_cursor.fetchone()
    print(result)
    if result:
        print(f"Salary updated for the employee : {u_emp_id} and salary : {u_salary}")
    else:
        print(f"{u_emp_id} No Records found with this ID. Update Action Failed")

u_d_emp_id=input(">Do you want to delete any employee . Kindly Enter your Emp Id: ")

def delete_employee(u_d_emp_id):
    db_cursor.execute("Select * from workers where id= %s", (u_d_emp_id,))
    result = db_cursor.fetchone()
    print(f"selected User EMP ID to delete :: {result}")
    if result:
        print(f" id :{u_d_emp_id} - found proceeding with deletion")
        delete_query=("Delete from workers where id =%s")
        db_cursor.execute(delete_query,(u_d_emp_id,))
        my_db.commit()
        print(f" id :{u_d_emp_id} deleted successfully ")
        db_cursor.execute("Select * from workers")
        for y in db_cursor.fetchall():
            print(y)

    else:
       print(f"{u_d_emp_id} NO RECORDS found to delete . Action Failed")


up=update_salary(u_salary,u_emp_id)
de=delete_employee(u_d_emp_id)