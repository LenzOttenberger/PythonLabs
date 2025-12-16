import time


def timing(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result_of_func = func(*args, **kwargs)
        end_time = time.time()
        final_time = (end_time - start_time) * 1000
        print(f'{func.__name__}() выполнилась за {final_time:.2f} мс!')
        return result_of_func
    return wrapper


@timing
def greeting(name):
    return f'Hello! My name is {name}'


print(greeting('James'))
