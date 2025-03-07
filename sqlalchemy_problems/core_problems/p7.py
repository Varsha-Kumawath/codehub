# 7. Join Query (Medium–Hard)
# Task:
# Define a second table department with columns:
# dept_id: Integer primary key
# dept_name: String
# Insert sample data into both employee and department (link employee.department with department.dept_name).
# Write a join query that retrieves each employee along with the corresponding department details.
#
# Requirement:
# Use SQLAlchemy Core’s join() and select() functions.
#
# Hint:
# Use employee.join(department, employee.c.department == department.c.dept_name).
#
#

import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, insert ,select
from sqlalchemy.exc import SQLAlchemyError

db_engine=create_engine('sqlite:///example.db')

metadata=MetaData()

employee=Table('employee',metadata,autoload_with=db_engine)

department=Table(
    'department',
    metadata,
    Column('dept_id', Integer, primary_key=True),
    Column('dept_name',String)
)

metadata.create_all(db_engine)

insert_employee_record=insert(employee).values(id=10, name='varsha', department='HR', salary=80000)
data=[{'dept_id':100,'dept_name':'Dev'},
      {'dept_id':101,'dept_name':'HR'}]
insert_department_record=insert(department)

join_query= select(employee,department).select_from(employee.outerjoin(department, employee.c.department == department.c.dept_name))

with db_engine.connect() as connection:
    trans=connection.begin()
    try:
        connection.execute(insert_employee_record)
        connection.execute(insert_department_record,data)
        result= connection.execute(join_query)
        trans.commit()
        for de in result:
            print(de)


    except SQLAlchemyError as e:
        trans.rollback()
        print(e)

