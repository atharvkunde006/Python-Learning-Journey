a=int(input("Enter a first number: "))
b=input("Enter the operator: ")
c=int(input("Enter a second number: "))
match b:
    case "+":
        print("Ans is:",a+c)

    case "-":
        print("Ans is:",a-c)
    
    case "*":
        print("Ans is:",a*c)

    case "/":
        print("Ans is:",a/c)