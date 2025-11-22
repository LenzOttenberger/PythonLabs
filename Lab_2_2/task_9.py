def type_check(*dec_args, **dec_kwargs):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for arg, dec_arg in zip(args, dec_args):
                if not isinstance(arg, dec_arg):
                    raise TypeError(
                        f'Аргумент {arg} не соответствует заявленному типу {dec_arg}')
            return func(*args, **kwargs)
        return wrapper
    return decorator


@type_check(str)
def greeting(name):
    return f'Hello! My name is {name}'


print(greeting('James'))
