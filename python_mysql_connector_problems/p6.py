# 6. Use Prepared Statements to Prevent SQL Injection (Medium)
#
# Description: Modify the insert script to use prepared statements
# and parameterized queries to prevent SQL injection attacks. Test it with different inputs to confirm security measures.


import mysql.connector

my_db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Varsha1057@#",
    database="mysqldemodb"
)

my_cursor=my_db.cursor()

U_name= input("> Enter your name:  ")
U_salary=input("> Enter your salary:  " )
U_department=input("> Enter your Department:  ")

query="INSERT INTO workers (name,salary,department) values (%s,%s,%s) "
my_cursor.execute(query,(U_name,U_salary,U_department))
my_db.commit()
my_cursor.execute("select * from workers")
for x in my_cursor.fetchall():
    print(x)