# 9. Subquery and Filtering (Hard)
# Task:
# Create a subquery that computes the average salary for each department from the employee table.
# Then write a main query to select all employees whose salary is above the department’s average.
#
# Requirement:
# Use a Core subquery and then join or filter against it.
#
# Hint:
# Use subq = select(employee.c.department, func.avg(employee.c.salary).label("avg_salary")).group_by
#     (employee.c.department).subquery() and then filter with a join condition.

from sqlalchemy import create_engine , MetaData ,select ,func

engine=create_engine('sqlite:///example.db')

metadata=MetaData()

metadata.reflect(bind=engine)

employee=metadata.tables['employee']
department=metadata.tables['department']

avg_subquery=(select (
        employee.c.department,func.avg(employee.c.salary).label('avg_salary')
).group_by(employee.c.department).
           subquery())

main_query=(
    select(employee
           .join(avg_subquery,employee.c.department== avg_subquery.c.department))
           .where(employee.c.salary > avg_subquery.c.avg_salary)
)

with engine.connect() as con:
    result = con.execute(main_query)
    for x in result:
        print(x)

