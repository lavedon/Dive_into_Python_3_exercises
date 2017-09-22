def make_counter(x):
    print('entering make_counter')
    while True:
            yield x
            print('incrementing x')
            x = x + 1

            
# makes a generator that adds 1 to whatever number you pass it
#
# “yield” pauses a function. “next()” resumes where it left off.
#
#
# Example:
# counter = make_counter(5):
# next(counter)
# next(counter)
# yada, yada, yada
