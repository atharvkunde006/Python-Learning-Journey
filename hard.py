#count even odd numbers 1to n
n=int(input("Enter the numbers:"))
i=1
while(i<=n):
    if(i%2==0):
        print(i,"even")
        i=i+1
    else:
        print(i,"odd")
        i=i+1

#reverse the number
i=321
while(i>123):
        print(i)
        i=i-1

#password game
a=1234
while(True):
     password=int(input("Enter the password:"))
     if(password==a):
          print("Welcome to the game!!")
          break
     else:
          print("wrong password!! Try again!!") 