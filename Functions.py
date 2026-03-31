
# x = int(input("Enter a number: "))

# def square(x):
#     print(f"The square of {x} is {x**2}")
# square(x)

# def addNum (a, b):
#     return a + b
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# result = addNum(num1, num2)
# print(f"The sum of {num1} and {num2} is {result}")

# import math

# print(round(math.pi, 2))

# cube = lambda x: x**3
# num = int(input("Enter a number to find its cube: "))
# print(f"The cube of {num} is {cube(num)}")

# def sum_all (*args):
#     return sum(args)
# print(sum_all(1, 2, 3, 4, 5))


# def kargs_example(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# kargs_example(name="Alice", age=30, city="New York")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))

