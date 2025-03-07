# ///3. Batch Insertion (Easy–Medium)
#
# Task:
# Insert multiple employee records into the employee table in a single transaction. Provide at least three records.
#
# Requirement:
# Use a list of dictionaries with column-value pairs.
#
# Hint:
# Use the same insert(employee) statement with a list passed as the second argument to execute().
#

import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, insert ,select
from sqlalchemy.exc import SQLAlchemyError

db_engine=create_engine('sqlite:///example.db')

metadata=MetaData()

employee=Table('employee',metadata,autoload_with=db_engine)


# Data to be inserted (list of dictionaries)
data = [
    {'id':2, 'name':'Jaga', 'department':'Dev','salary':50000},
    {'id':3, 'name':'Jagadhish', 'department':'Dev','salary':32000.25},
    {'id':4, 'name':'Jazz', 'department':'Dev','salary':140000.78},
]

# Build an INSERT query
insert_batch_records=insert(employee)


with db_engine.connect() as connection:
    trans=connection.begin()
    try:
        connection.execute(insert_batch_records,data)
        trans.commit()

        query = select(employee)
        result = connection.execute(query)
        for row in result:
            print(row)

    except sqlalchemy.exc.SQLAlchemyError as e :
        trans.rollback()
        print(e)

