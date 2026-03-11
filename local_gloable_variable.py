#
x=10
def my_function():
    y=5
    print(y)
my_function()
print(x)

##
x=10
def my_function():
    global x
    x=5
y=5
my_function()
print(x)
print(y)

