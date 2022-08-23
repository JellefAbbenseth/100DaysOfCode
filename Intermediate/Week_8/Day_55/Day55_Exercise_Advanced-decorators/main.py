def logging_decorator(function):
    def wrapper_function(*args, **kwargs):
        result = function(args)
        print(f"You called {function.__name__}", end="(")
        for i in range(len(args)):
            if i + 1 == len(args):
                print(str(args[i]), end=")\n")
            else:
                print(str(args[i]), end=", ")
        print(f"It returned: {result}")

    return wrapper_function


@logging_decorator
def a_function(*args):
    number = 0
    for num in args[0]:
        number += num
    return number


a_function(1, 2, 3)
