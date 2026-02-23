for i in range(2,11,1):
    if(i%2==0):
        continue
    print(i)

for i in range(12):
    if(i==10):
        print("skip the iteration")
        continue
    print("5",i,"=",5*i)