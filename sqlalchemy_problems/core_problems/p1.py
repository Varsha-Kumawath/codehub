# 1. Table Definition and Creation (Easy)
# Task:
# Create an SQLite engine and a MetaData object. Define a table called employee with the following columns:
#
# id: Integer primary key
#
# name: String
#
# department: String
#
# salary: Numeric
#
# Requirement:
# Use the SQLAlchemy Core Table construct and then call metadata.create_all(engine) to create the table.
#
# Hint:
# Use from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Numeric.

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Numeric

# Create an engine to connect to the database
db_engine=create_engine('sqlite:///example.db')

#create Metadata object
metadata=MetaData()

#create table explicitly
employee= Table (
    'employee',
    metadata,
    Column('id',Integer , primary_key=True),
    Column('name',String(50)),
    Column('department',String(50)),
    Column('salary',Numeric(10))
)


metadata.drop_all(db_engine)  # Drops all tables defined in metadata  only use when schema is already created
# Create the table in the database
metadata.create_all(db_engine)



