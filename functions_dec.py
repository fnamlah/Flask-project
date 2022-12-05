# Functions are first-class objects, can be passed around as arguments e.g. int/string/float etc.
# def add(n1, n2):
#     return n1 + n2
#
#
# def calculate(calc_function, n1, n2):
#     return calc_function(n1, n2)
#
#
# print(calculate(add, 2, 3))

# Nested Functions:
# def outer_function():
#     print("i'm outer")
#
#     def nested_function():
#         print("i'm inner")
#
#     nested_function()
#
#
# outer_function()

# functions returned from other functions
# def outer_function():
#     print("i'm outer")
#
#     def nested_function():
#         print("i'm inner")
#
#     return nested_function
#
#
# inner_function = outer_function()
# inner_function()

## Simple Python Decorator Functions
import time


def delay_decorator(function):
    def wrapper_function():
        time.sleep(5)
        # Do something before
        function()
        function()
        # Do something after

    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello")


# With the @ syntactic sugar
@delay_decorator
def say_bye():
    print("Bye")


# Without the @ syntactic sugar
def say_greeting():
    print("How are you?")


# decorated_function = delay_decorator(say_greeting)
# decorated_function()
say_hello()