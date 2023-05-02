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
