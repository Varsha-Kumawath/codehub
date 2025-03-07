# 5. Updating Records (Medium)
#
# Task:
# Update the salary of a specific employee (for example, update the employee with id=1 to a salary of 55000).
#
# Requirement:
# Write and execute a Core UPDATE statement and then verify the update with a SELECT.
#
# Hint:
# Use update(employee).where(employee.c.id == 1).values(salary=55000).

from sqlalchemy import update ,select
from sqlalchemy.exc import SQLAlchemyError

from sqlalchemy_problems.core_problems.p2 import db_engine,employee

update_query=update(employee).where(employee.c.id == 1).values(salary=55000)
with db_engine.connect() as connection:
    trans=connection.begin()
    try:
        connection.execute(update_query)
        trans.commit()
        query = select(employee)
        result = connection.execute(query)
        for row in result:
            print("After updating ")
            print(row)

    except SQLAlchemyError  as e:
        trans.rollback()
        print(e)

