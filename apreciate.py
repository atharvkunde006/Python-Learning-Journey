a=int(input("Enter your grade:"))
match a:
    case a if a >= 90:
        print("you are excellent")
    case b if b >= 80:
        print("you are good")
    case c if c>=70:
        print("you are average")