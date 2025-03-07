# 8. Aggregation Query (Medium–Hard)
#
# Task:
# Using the employee table, write a query to calculate the total salary expenditure per department.
#
# Requirement:
# Group by the department column and sum the salaries.
#
# Hint:
# Use func.sum() from SQLAlchemy along with group_by(employee.c.department).

import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table ,select , func
from sqlalchemy.exc import SQLAlchemyError

engine=create_engine('sqlite:///example.db')

metadata=MetaData()

# Reflect all tables from the database into metadata.tables
metadata.reflect(bind=engine)

# Access the tables by name
employee = metadata.tables['employee']
department = metadata.tables['department']

cal_query=select(
    employee.c.department,
    func.sum(employee.c.salary).label('total_salary')
).group_by(employee.c.department)


with engine.connect() as conn:
    try:
        result=conn.execute(cal_query)
        for x in result.fetchall():
            print(x)
    except SQLAlchemyError as e:
        print(e)
