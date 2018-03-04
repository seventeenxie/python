import time


def decorator(fun):
    print("decorator")
    return fun


def print_function(a):
    time.sleep(2)
    print("print_function seleep 3 seconds")
    print(a)


mydecorator = decorator(print_function)
mydecorator("fsdsdf");
