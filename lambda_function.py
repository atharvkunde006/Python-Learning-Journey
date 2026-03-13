#
file=lambda a,b:a+b
print(file(5,5))

##
squre=lambda a:a*a
print(squre(5))

##
num=[5,6,5,8]
result=list(map(lambda x:x*2,num ))
print(result)

####
num=(2,5,3,7)
result=tuple(map(lambda x:x+1,num))
print (result)

#####
num=[1,5,8,9]
result=list(filter(lambda x:x%2==0,num))
print(result)

#####
a=[1,2,3,4]
b=[1,2,3,4]
result=list(map(lambda x,y:x+y,a,b))
print(result)

#####
a=[12,34,56,76,54,32,12]
result=list(filter(lambda x : x>15 and  x<17 ,a))
print(result)

######
num=[1,2,3,4,5,6,7,8]
result=list(map(lambda x:x*2 , filter(lambda x:x%2==0,num)))
print(result)