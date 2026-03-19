#
def greet (fx):
    def mfx():
        print("Good Morning")
        fx()
        print("Thanks for using this function")
    return mfx
@greet
def hello ():
 print("Hello World")
def add(a,b):
 print(a+b)
hello()

##
import logging
def log_function_call(func):
    def decorated(*args,**kwargs):
       logging.info(f"calling {func.__name__} with args={args},kwargs={kwargs}")
       result=func(*args,**kwargs)
       logging.info(f"{func.__name__} return {result}")
       return result
    return decorated
@log_function_call
def my_function(a,b):
 return a+b

###
def greet(x):
    def func():
        print("Hii Atharv")
        x()
        print("i am fine")
    return func
@greet
def ak():
 print("Hello!!")
ak()