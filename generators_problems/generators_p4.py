# Infinite Arithmetic Sequence Generator
#
# Problem Statement:
#
# Implement a generator arithmetic_sequence(start, step) that:
#
# Starts from start and generates numbers by adding step on each iteration.
#
# Yields an infinite arithmetic sequence like:
#
# arithmetic_sequence(2, 3) → 2, 5, 8, 11, 14, …
#
#
# Ensure lazy evaluation without using large lists.

def arithmetic_sequence(start, step):

    while True:
        start += step
        yield start


a=arithmetic_sequence(2,3)
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())