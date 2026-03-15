print("Welcome to our shop!!")
sum=0
a=input("Enter the costomer name:\n")
pin=1234
b=int(input("Enter the pin number:\n"))
if(b==pin):
    print(f" Wellcome!!{a} you are allow in shop..")
    item=1
    while True:
        print(f"item no:{item}")
        user=input("Enter your price and press q for stop: \n")
        if(user!='q'):
            sum=sum+int(user)
            print("The total is:",sum)
            item+=1
        else:
            print(f"your bill is :{sum}")
            print(f"Thank you for visit")
            break
else:
    
        print("your not allow!!")
        print("please leave the shop.")