# Execution Time Logger
#
# Problem Statement:
#
# Write a decorator @log_execution_time that:
#
# Measures and logs the execution time of the decorated function.
#
# Prints something like:
#
# Function foo executed in 2.35 seconds
#
#
# Should work with any function that takes any number of arguments.
#
# Ensure reusability across multiple functions.

import time
# import functools

def log_execution_time(func):
    # @functools.wraps(func)  # Preserves the original function metadata
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record start time
        result = func(*args, **kwargs)  # Execute the function
        end_time = time.time()  # Record end time
        execution_time = end_time - start_time  # Calculate execution duration
        print(f"Function {func.__name__} executed in {execution_time:.4f} seconds")
        return result  # Return the original function's output
    return wrapper

# Example usage:
@log_execution_time
def sample_function(n):
    time.sleep(n)  # Simulating a time-consuming process
    return "Execution Completed!"

# Call the decorated function
print(sample_function(2))
