#print name
def name():
    print("atharv")
name()

# add two numbers
def add(a,b):
    print(a+b)
a=5
b=10
add(a,b)
add(a,b)

#even odd numbers
def even_odd(num):
 if num%2==0:
        print("even")
 else:
     print("odd")
num=7
even_odd(num)
num=8
even_odd(num)

#squre of a number
def sqr(num):
    print(num*num)
num=5
sqr(num)

#multiplication table
def table(num):
    for i in range(1,11):
     print(num,"*",i,"=",num*i)
num=5
table(num)