import time

# example one

def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        # print(f"{func.__name__} ran in {end - start}")
        return result
    return wrapper

@timer
def example_func(n):
    time.sleep(n)
    
# example_func(2)


# example two

def debug(func):
    def wrapper(*args,**kwargs):
        args_val = ', '.join(str(arg) for arg in args)
        kwargs_val = ', '.join(f"{k} {v}" for k,v in kwargs.items())
        print(f"calling : {func.__name__} with args val {args_val} kwargs {kwargs_val}")
        return func(*args,**kwargs)
    return wrapper


def greeting(name,greeting="hello"):
    print(f"{name} {greeting}")
    
# greeting("john")


# example 3


def cache(func):
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper

@cache
def plus(a, b):
    time.sleep(4)
    return a + b

print(plus(3,2))
print(plus(7,2))