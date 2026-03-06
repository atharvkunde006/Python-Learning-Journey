#
fruits=["mango","banana","apple","pinaple"]
for index,fruit in enumerate(fruits):
    print(index,fruit)

##
furits=["banana","apple","mango","chuku"]
for index,fruit in enumerate(fruits,start=1):
    print(index,fruit)

###
marks=[12,56,32,98,12,45,1,4]
for index,mark in enumerate(marks,start=1):
    print(mark)
    if(index==3):
        print("Atharv is awesome!!")