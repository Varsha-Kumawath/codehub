# Memoization for Expensive Function Calls
#
# Problem Statement:
#
# Implement a decorator @memoize that:
#
# Caches the results of expensive function calls.
#
# If a function is called with the same arguments again, it returns the cached result instead of recomputing.
#
# Works for any function with hashable arguments.
#
# This is useful for optimizing recursive functions like Fibonacci.
#
#

import functools

def memoize(func):
    cache = {} # Dictionary to store computed results

    @functools.wraps(func)  # Preserve function metadata
    def wrapper(*args):
        if args in cache:  # Check if result is already cached
            print(f"Fetching from cache for {args}")
            return cache[args]
        else:
            print(f"Computing result for {args}")
            result = func(*args)  # Compute and store in cache
            cache[args] = result
            return result

    return wrapper

# Example: Expensive Fibonacci computation
@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Test the memoization
print(fibonacci(3))  # Cached calls will speed up execution
