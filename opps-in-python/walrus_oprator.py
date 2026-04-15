#
number=[1,2,3,4,5]
while (n:=len(number))>0:
    print(number.pop())

##
names=["jhon","jane","jim"]
if(name:=input("Enter a name:"))in names:
    print(f"Hello,{name}!")
else:
    print("name not found.")

###
foods=list()
while (food:=input("what food do you like :"))!="quit":
       foods.append(food)
    