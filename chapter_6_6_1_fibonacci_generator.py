def fib(max):
    a, b = 0, 1 # a = 0.  b = 1. The start of the Fibonacci sequence.
    while a < max:
        yield a   # returns the current number in the sequence. Then pauses.
        a, b = b, a + b # 1) a = b. 2) b = a + b. Note: This is done in parallel.

    # Here is a longer discussion of the above (from the book):
    # 	b is the next number in the sequence, so assign that to a,
    #   but also calculate the next value (a + b) and assign that to b for later use.
    #   Note that this happens in parallel; if a is 3 and b is 5, then a, b = b, a + b will set a to 5 (the previous value of b) and b to 8 (the sum of the previous values of a and b).


# Remember:
# "yield" pauses a function.
# "next()" resumes where it left off.
#
# How to use:
# nums = fib(30)
# next(nums)
#
# example with for loops
# for n in fib(1000):
#     print(n, end=' ')  # end=' ' adds in some whitespace stuff.
#
# Way to use this to make a neat list:
# list(fib(1000))
