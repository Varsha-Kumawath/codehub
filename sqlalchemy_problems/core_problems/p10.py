# 10. Using Textual SQL with Bind Parameters (Hard)
#
# Task:
# Write a raw SQL query as a string to select employees with a salary greater than a specified value. Bind the value as a parameter.
#
# Requirement:
# Execute the textual SQL query and print the results.
#
# Hint:
# Use text("SELECT * FROM employee WHERE salary > :min_salary") and pass the parameter as {"min_salary": 60000}.

from sqlalchemy import create_engine, MetaData, text

engine=create_engine('sqlite:///example.db')
metadata=MetaData()


metadata.reflect(bind=engine)

emp=metadata.tables['employee']
dep=metadata.tables['department']

query=text('select * from employee where salary > :min_salary')

with engine.connect() as con:
    result= con.execute(query,{'min_salary': 60000})
    for row in result.fetchall():
        print(row)