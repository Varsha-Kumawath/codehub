#
# 4. Selecting Records (Easy)
#
# Task:
# Write a SELECT query using SQLAlchemy Core to fetch all rows from the employee table.
#
# Requirement:
# Fetch and print the results.
#
# Hint:
# Use select(employee) and then connection.execute(query).fetchall().

import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table ,select
from sqlalchemy.exc import SQLAlchemyError

db_engine=create_engine('sqlite:///example.db')

metadata=MetaData()

employee=Table('employee',metadata,autoload_with=db_engine)


with db_engine.connect() as connection:
    trans=connection.begin()
    try:
        query = select(employee)
        result = connection.execute(query)
        for row in result.fetchall():
            print(row)

    except sqlalchemy.exc.SQLAlchemyError as e :
        trans.rollback()
        print(e)

