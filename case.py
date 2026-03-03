try :
   a=int(input("Enter the first number:" ))
   b=input("Enter the oprator:" )
   c=int(input("Enter the second number: "))
   match b:
     case "+":
         print(a+c)
     case "-":
         print(a-c)
     case "*":
         print(a*c)
except ValueError :
 print("!!! WARNING !!! print valid number")