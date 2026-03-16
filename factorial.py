while True:
 def factorial(number):
    if (number==1 or number==0):
        return 1
    else:
     return number*factorial(number-1)
 number=int(input("Enter the number"))
 fact=factorial(number)
 print(fact)
