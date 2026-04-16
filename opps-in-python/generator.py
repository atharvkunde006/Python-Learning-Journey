#
def my_generator():
    for i in range(5):
        yield i
gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

##
gen = my_generator()
for i in gen:
    print(i)
    
###
def count(n):
    for i in range(n):
        yield i

for num in count(5):
    print(num)