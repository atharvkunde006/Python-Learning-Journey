#
a=[1,2,3,4]
b=[1,2,3,4]
print(a==b)
print(a is b)

##
a=10
b=10
print(a == b)
print(a is b)

###
a=20
b=30
print(a==b)
print(a is b)


import random

num = random.randint(1,10)

guess = int(input("Guess number 1-10: "))

if guess == num:
    print("Correct!")
else:
    print("Wrong, number was",num)