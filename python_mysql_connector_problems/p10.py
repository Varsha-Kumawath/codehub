# 10. Connection Pooling for Performance Optimization (Very Hard)
#
# Description: Implement a connection pool using mysql.connector.pooling.MySQLConnectionPool.
# Create a pool of 5 connections and execute multiple queries using different connections from the pool.
# Measure the execution time and compare it with a normal connection approach.

import mysql.connector
from mysql.connector import pooling
import time

db_pool=pooling.MySQLConnectionPool(
    pool_name="mydbpool",
    pool_size=5,  #Use buffered=True when fetching large datasets.
    buffered=True,
    host="localhost",
    user="root",
    password="Varsha1057@#",
    database="mysqldemodb"
)

print("Connection Pool Created Successfully!")


def execute_query_with_pool(query):
    try:
        db_con = db_pool.get_connection()  # Get a connection from the pool
        dbpool_cursor = db_con.cursor()
        dbpool_cursor.execute(query)
        results_with_pool=dbpool_cursor.fetchall()
        # print(f"Pool : {results_with_pool}")
        return  results_with_pool

    except mysql.connector.errors as e:
        print(e)


def execute_query_without_pool(query):
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Varsha1057@#",
            database="mysqldemodb"
        )

        db_cursor = db.cursor()
        db_cursor.execute(query)
        results_without_pool=db_cursor.fetchall()
        # print(f"Without Pool :{results_without_pool}")
        return  results_without_pool

    except mysql.connector.errors as e:
        print(e)

query="SELECT * FROM workers"

#calculating the pool execution time

start_time_with_pool=time.time()
execute_query_with_pool(query)
end_time_with_pool=time.time()

pooling_execution_time=end_time_with_pool - start_time_with_pool
print(f"Execution Time w.r.t pool : {pooling_execution_time:.4f}")

# Calculating the without pool execution time

start_time_without_pool = time.time()
execute_query_without_pool(query)
end_time_without_pool = time.time()

normal_execution_time =end_time_without_pool-start_time_without_pool
print(f"Execution Time w.r.t without pool : {normal_execution_time:.4f}")

#conculde which is efficient
if pooling_execution_time<normal_execution_time:
    print(f"Pooling execution - {pooling_execution_time:.4f} is taking less time than normal execution - {normal_execution_time:.4f}")
else:
    print(f"normal execution - {normal_execution_time:.4f} is taking less time than Pooling execution - {pooling_execution_time:.4f}")




