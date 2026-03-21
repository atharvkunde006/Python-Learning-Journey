#
def deco(func):
    def wrapper(*args,**kwargs):
        print("Before function")
        result=func(*args,**kwargs)
        print("After function")
        return result
    return wrapper
@deco
def add(a,b):
    return a+b
print(add(2,5))

##
def required_role(role):
    def decorators(func):
        def wrapper(user):
            if user!=role:
                print("Access Denied")
                return
            return func(user)
        return wrapper
    return decorators
@required_role("admin")
def dashboard(user):
 print("Welcome to dashboard")
dashboard("admin")
dashboard("guest")

###
def start(x):
    def stop():
     print("start")
    (x)
    print("End")
    return stop
@start
def func():
 print("car")
func()

####
def counter(func):
    count=0
    def wrapper(*args,**kwargs):
        nonlocal count
        count+=1
        print(f"called {count} times")
        return func(*args,**kwargs)
    return wrapper
@counter
def greet():
 print("hii")
greet()
greet()