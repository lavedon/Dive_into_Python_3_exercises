# Chapter 6_4 Dive Into Python 3

def first_func():
    print("First function happened")

def second_func():
    print("Second function happened")

def third_func():
    print("Third function happened")
    print("Which is fun.")
    a = 1 + 2 + 3
    print(a)
    print("Functions do things.")
    print("That is all...")

tupleOFunctions = (first_func, second_func, third_func)

for i in tupleOFunctions:
    i()

print("Do it as a list")
print("\n \n \n \n \n \n")

listOFunctions = [first_func, second_func, third_func]

for y in listOFunctions:
    y()
