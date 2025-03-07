# 6. Deleting Records (Medium)
#
# Task:
# Delete an employee record (for example, where the name is 'Alice').
#
# Requirement:
# Use a Core DELETE statement and confirm deletion with a SELECT.
#
# Hint:
# Use delete(employee).where(employee.c.name == 'Alice').

import sqlalchemy
from sqlalchemy import delete, MetaData, create_engine, Table, select, bindparam
from sqlalchemy.exc import SQLAlchemyError


db_engine=create_engine('sqlite:///example.db')

metadata=MetaData()

employee=Table('employee',metadata,autoload_with=db_engine)

delete_query=delete(employee).where(employee.c.name.in_(bindparam("name", expanding=True)))

with db_engine.connect() as connection:
    trans=connection.begin()
    try:
        connection.execute(delete_query,{'name':('Jaga',)})
        trans.commit()
        # Confirm deletion:
        query = select(employee).where(employee.c.name == 'Jaga')
        result = connection.execute(query).fetchall()
        if result:
            print(result)
            print('Deletion action is not reflected in back end')
        else:
            print("Deleted the record")
            query = select(employee)
            re = connection.execute(query)
            for x in re.fetchall():
                print(x)


    except SQLAlchemyError as e:
        print(e)
        trans.rollback()
