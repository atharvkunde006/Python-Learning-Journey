#first program
x=int(input("Enter the value of x:"))
match x:
        case 0:
         print("x is zero")
        case 4:
         print("x is 4")
        
#second program
x=int(input("Eneter the value of x:"))
match x:
   case 0:
      print("x is zero")
   case 4:
      print("case is 4")
   case _if !=90:
      print(x,"is not 90")
