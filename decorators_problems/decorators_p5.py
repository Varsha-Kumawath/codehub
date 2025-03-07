# Logging Function Calls
#
# Problem Statement:
#
# Write a decorator @log_function_call that:
#
# Logs every call to a function with its arguments and return value.
#
# Example log:
#
# Calling function: multiply(3, 5)
# Function returned: 15
#   Ensure it works with any function.

import functools
def log_function_call (func):
    @functools.wraps(func)  # Preserve function metadata
    def decorator(*args, **kwargs):
        print(f"Calling function: {func.__name__}{args} {kwargs}")  # Log function call
        result = func(*args, **kwargs)  # Call the actual function
        print(f"Function returned: {result}")  # Log return value
        return result  # Return the actual result

    return decorator

@log_function_call
def multiply(a,b):
    return a*b


# Test cases
multiply(b=55 ,a=75)
multiply(7, 2)


