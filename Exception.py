a=input("Enter the number")
print(f"multiplicatin table of{a}:")
try:
    for i  in range(1,11):
        print(f"{int(a)}x{int(i)}={int(a)*i}")
except Exception as e:
 print(e)
 print("some imp line of code")
 print("End of program")