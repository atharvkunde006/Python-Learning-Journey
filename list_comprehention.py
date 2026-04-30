#
list=[i*2 for i in range (10)]
print (list)

##
even=[i for i in range(10) if i%2==0]
print(even)

###
a=["even" if x%2==0 else "odd" for x in range (5) ]
print(a)

####
pairs = [(x, y) for x in range(2) for y in range(3)]
print(pairs) 

#####
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print(upper_words)  

######
import time

# Using a for loop
start = time.time()
squares_loop = []
for x in range(10**6):
    squares_loop.append(x**2)
print("Loop time:", time.time() - start)

# Using list comprehension
start = time.time()
squares_comp = [x**2 for x in range(10**6)]
print("List Comprehension time:", time.time() - start)
