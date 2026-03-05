#
try:
    a=int(input("enter the number:"))
except ValueError:
    print("This is wrong value!!")

##
try:
    a=int(input("Enter the name: "))
except ValueError as e:
    print(e)

###
a=input("Enter the number:")
print(f"multiplication table of {a}")
try:
  for i in range(1,11):
     print(f"{int(a)}x{i}={int(a)*i}")
except ValueError :
 print("The invalid number:")
