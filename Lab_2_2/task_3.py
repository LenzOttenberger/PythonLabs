import datetime


def log_calls(file_name):
    def log(func):
        def wrapper(*args, **kwargs):
            file = open(file_name, "a")
            file.write(f'Logging Time: {datetime.datetime.now().time()}, '
                       f'function {func.__name__}(), '
                       f'args: {args, kwargs}.\n')
            file.close()
            return func(*args, **kwargs)
        return wrapper
    return log


@log_calls(file_name="log.txt")
def greeting(name):
    return f'Hello! My name is {name}'


print(greeting('James'))
