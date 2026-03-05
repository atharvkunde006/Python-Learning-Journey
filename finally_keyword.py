#
try:
    a=int(input("Enter the number:"))
except ValueError:
    print("The invalid number:")
finally:
    print("Me hamesha print hoga!!")

##
try:
     a=int(input("Enter the number:"))
     print(f"The multiplicatin table of {a}")
     for i in range(1,11):
        print(f"{int(a)}x{i}={int(a)*i}")
except ValueError:
        print("invalid number")
finally:
        print("This is a multilication table of",(a))