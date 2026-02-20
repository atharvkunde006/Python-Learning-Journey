a=int(input("Enter a number:"))
match a:
    case 1:
        print("a is one")
    case 2:
        print("a is two")
    case 3:
        print("a is three")
    case _:
        print("a is not 1, 2, or 3")