cache_dict = {}


def cache(func):
    def wrapper(*args):
        if args not in cache_dict:
            cache_dict[args] = func(*args)
            return func(*args)
        else:
            return cache_dict[args]
    return wrapper


@cache
def summ(a, b):
    return a + b


for i in range(5):
    print(summ(i+1, i+2))

for i in range(5):
    print(summ(i+1, i+2))
