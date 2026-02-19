a=int(input("Enter the first number: "))
operator=input("Enter the operator : ")
b=int(input("Enter the second number: "))
if operator=="+":
    print(a+b)
elif operator=="-":
    print(a-b)
elif operator=="*":
    print(a*b)
elif operator=="/":
    print(a/b)
else:
    print("Invalid operator")