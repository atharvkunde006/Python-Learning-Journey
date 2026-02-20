a=int(input("Enter your number :"))
match a:
    case 90|91|92|93|94|95|96|97|98|99|100:
        print("your grade is A")
    case 80|81|82|83|84|85|86|87|88|89:
        print("your grade is b")
    case 70|71|72|73|74|75|76|77|78|79:
        print("your grade is c")
    case 1|60:
        print("you are fail")
        