import time


def decorator(fun):
    def decorator(*args, **kwargs):
        fun(*args, **kwargs)
        print(*args)

    print("decorator")
    return decorator


def print_function(a):
    time.sleep(2)
    print("print_function seleep 3 seconds")
    print(a)


fun = decorator(print_function)
fun("a")
