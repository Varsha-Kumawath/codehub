# 9. Stored Procedure Execution in Python (Hard)
#
# Description: Create a stored procedure in MySQL
# that takes an employee ID and returns their details. Write a Python script to call this stored procedure and display the result.

import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Varsha1057@#",
    database="mysqldemodb"
)

db_cursor=db.cursor()

emp_id=input("> Enter Emp Id:  ")

#Create a Stored Procedure in SQL

stored_procedure = """
CREATE PROCEDURE GetEmployeeDetails(IN emp_id INT)
BEGIN
    SELECT * FROM workers WHERE id = emp_id;
END;
"""
# db_cursor.execute(stored_procedure) # once executed , it will be created no need to create again

print(" Stored Procedure 'GetEmployeeDetails' Created Successfully!")

try:
    #Call the stored procedure
    db_cursor.callproc("GetEmployeeDetails", (emp_id,))

    # Fetch results
    for result in db_cursor.stored_results():
        employee = result.fetchone()
        if employee:
            print(f"Employee Found: {employee}")
        else:
            print("Employee Not Found!")

except mysql.connector.Error as e:
    print(f"Error executing stored procedure: {e}")

