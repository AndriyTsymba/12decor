
#1

def my_decorator_func(func):
    def wrapper():
        print(10+10)
        func()
    return wrapper()
@my_decorator_func
def say_hellow():
    print()

#2
import time
def time_fuction(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        result = func(*args,**kwargs)
        end_time = time.time()
        print("Час виконнання функції",end_time - start_time)
        return result
    return wrapper()
@time_fuction
def example_fuction(x):
    time.sleep(1)#pass
    return x
print(example_fuction())
#3
def cache(func):
    cache_dict ={}
    def wrapper(*args,**kwargs):
        if args in cache_dict:
            return cache_dict[args]
        else:
            result= func(*args)
            cache_dict[args] = result
            return result,cache_dict
    return wrapper()
@cache
def my_fuction(x,y):
    return x*y
print(my_fuction(3,10))
#4
def logger(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        print(f"Функція" {func._name_},"Аргумент" {args},"результат" {result})
        return result
    return wrapper()
@logger
def my_dict(x,y):
    return x+y
print(my_fuction(10,20))