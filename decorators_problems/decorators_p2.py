# Retry on Failure
#
# Problem Statement:
#
# Write a decorator @retry_on_failure(retries=3) that:
#
# Retries the decorated function up to retries times if it raises an exception.
#
# If the function succeeds, it returns the result.
#
# If it still fails after all retries, it raises the final exception.
#
# This is useful for handling network failures or unreliable APIs.


import time
import functools

def retry_on_failure(retries=3, delay=1):
    def decorator(func):
        @functools.wraps(func)  # Preserves original function metadata
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < retries:
                try:
                    return func(*args, **kwargs)  # Try executing the function
                except Exception as e:
                    attempts += 1
                    print(f"Attempt {attempts} failed: {e}")
                    if attempts < retries:
                        print(f"Retrying in {delay} seconds...")
                        time.sleep(delay)  # Wait before retrying
                    else:
                        print("All retries failed. Raising final exception.")
                        raise  # Raise final exception after all attempts
        return wrapper
    return decorator

# Example usage:
import random

@retry_on_failure(retries=3, delay=2)
def unreliable_function():
    if random.random() < 0.7:  # 70% chance to fail
        raise ValueError("Random failure occurred!")
    return "Success!"

# Call the decorated function
print(unreliable_function())
