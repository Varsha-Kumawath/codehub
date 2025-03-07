# 2. Prime Number Generator
#
# Problem Statement:
#
# Create a generator function prime_generator() that yields infinite prime numbers.
#
# A prime number is a number greater than 1 that has only two divisors: 1 and itself.
#
# The generator should return the next prime number each time it is called using next().


def prime_generator(n):
    for num in range(2,n+1):
        if num == 2 or all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
             yield num


def infinite_prime():
    num=2
    while 1:
        if num == 2 or all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            yield num
        num+=1



p=infinite_prime()
print(p.__next__())









# Outer Loop: for num in range(2, n + 1)
# Iterates through numbers from 2 to n.
# Each num represents a potential prime number that we need to check.

# inner loop process
# all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
# Inner Loop: for i in range(2, int(num ** 0.5) + 1)
# Checks if num is divisible by any number i from 2 to √num.
# If num is not divisible by any i, then it's prime.


# Step-by-Step Execution
# Let's take n = 10 and analyze each step:
#
# num	range(2, int(num ** 0.5) + 1)	all(num % i != 0 for i in range(...))	Prime?
# 2	        -	                               num == 2, so it's prime	            ✅ Yes
# 3	      range(2, 2)                           (empty)	all([]) → True	            ✅ Yes
# 4	      range(2, 3) → [2]	                    4 % 2 == 0 (fails)	                ❌ No
# 5	      range(2, 3) → [2]	                    5 % 2 != 0 → True	                ✅ Yes
# 6	      range(2, 3) → [2]	                    6 % 2 == 0 (fails)	                ❌ No
# 7	      range(2, 3) → [2]	                    7 % 2 != 0 → True	                ✅ Yes
# 8	      range(2, 3) → [2]	                    8 % 2 == 0 (fails)	                ❌ No
# 9	      range(2, 4) → [2, 3]	                9 % 3 == 0 (fails)	                ❌ No
# 10	  range(2, 4) → [2, 3]	                10 % 2 == 0 (fails)	                ❌ No


# 🔹 Key Observations
# Outer Loop (num) iterates from 2 to n.
# Inner Loop (i) iterates only up to √num, reducing computations.
# The all() function ensures num is not divisible by any i, confirming primality.