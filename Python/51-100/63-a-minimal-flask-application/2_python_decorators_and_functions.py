## Functions can have inputs/functionality/output
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


##Functions are first-class objects, can be passed around as arguments e.g. int/string/float etc.


def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)


result = calculate(add, 2, 3)
print(result)


##Functions can be nested in other functions


def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    nested_function()


outer_function()

## Functions can be returned from other functions
def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    return nested_function


inner_function = outer_function()
inner_function


# <-------------------------------------------------------------------------------------------------------->

## Simple Python Decorator Functions
import time


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
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


decorated_function = delay_decorator(say_greeting)
decorated_function()


# <-------------------------------------------------------------------------------------------------------->
# # decorator function to print the run time of a function
def speed_calc_decorator(function):
    def wrapper_function():

        start_time = time.time()
        function()
        end_time = time.time()

        print(f"{function.__name__} run speed: {start_time - end_time}")

    return wrapper_function


# apply the decorator to the function
@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


# apply the decorator to the function
@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()


# <-------------------------------------------------------------------------------------------------------->

## Advanced Python Decorator Functions
# Checks if the user is logged in, when the function is called

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

new_user = User("Remen")
new_user.is_logged_in = True
create_blog_post(new_user)


# <-------------------------------------------------------------------------------------------------------->

# Advanced decorators using positional and keyword arguments

def logging_decorator(function):
    def wrapper_function(*args, **kwargs):
        print(f"You called {function.__name__}{args}")
        result = function(*args)
        
        print(f"It returned: {result}")
    return wrapper_function


# Use the decorator 👇
@logging_decorator
def a_function(*args):
    product = 1
    for i in args:
        product *= i
    
    return product


a_function(1, 2, 3)