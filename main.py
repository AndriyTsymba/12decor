#1


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
print(example_fuction(56))
