a=int(input("Enter a number:"))
match a:
    case _ if a%2==0:
        print (a,"is an even number")

    case _ if a%2!=0:
        print (a,"is an odd number")
