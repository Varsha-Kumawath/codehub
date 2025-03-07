def fibonacci_generator(n):
    first_num, second_num= 0, 1
    while range(0,n):
          yield first_num  #The generator remembers where it left off, so each call to next(fib) resumes execution after the last yield.
          first_num, second_num = second_num, first_num + second_num

# a, b = b, a + b:
# Updates a to the next number (b).
# Updates b to the sum of the previous two numbers (a + b).


f=fibonacci_generator(5)
print(f.__next__())

#
# for i in range(7):
#     print(next(f), end ="-")

