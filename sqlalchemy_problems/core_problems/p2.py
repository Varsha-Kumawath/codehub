# //2. Inserting Single Records (Easy)
#
# Task:
# Write an SQLAlchemy Core INSERT statement to add a single employee record (e.g. id=1, name='Alice', department='HR', salary=50000) into the employee table.
#
# Requirement:
# Execute the insert statement using the connection.
#
# Hint:
# Use insert(employee).values(...) and then call connection.execute().

from sqlalchemy import create_engine, MetaData ,Table ,insert ,select
from sqlalchemy.exc import SQLAlchemyError

db_engine=create_engine('sqlite:///example.db')

metadata=MetaData()

employee=Table('employee',metadata,autoload_with=db_engine)

insert_query=insert(employee).values(id=1, name='Alice', department='HR', salary=50000)


with db_engine.connect() as con:
    trans=con.begin()
    try:
        con.execute(insert_query)
        trans.commit()

        query = select(employee)
        result = con.execute(query)
        for row in result:
            print(row)
    except SQLAlchemyError as e:
        print(e)
        trans.rollback()

