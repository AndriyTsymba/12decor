#Теорія Декоратори


def my_decorator_func(func):#3
  def wrapper():#4
      print("шото там")
      func()
      print("і шо там")
  return wrapper
@my_decorator_func#2
def say_helow():#1
     print("hello")
say_helow()     
#2
import time
def delay_decorator(func):
  def wrapper(*args,**kwargs):
      time.sleep(3)
      return func(*args,**kwargs)
  return wrapper
@delay_decorator
def sleepy():
    print("я сплю")
sleepy()
#3
