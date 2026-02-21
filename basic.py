#print number from 1to 10.
for a in range(1,11):
 print(a)

 for a in range(10):
  print(a+1)

#print number reverse
for a in range(10,0,-1):
 print(a)

 #even odd number
 for a in range(1,50):
  if(a%2==0):
   print("even number",a)
  else:
   print ("odd number",a)

#table of number using input
a=int(input("Enter the number"))
for i in range(1,11):
 print(a*i)

# sum of first n number
n= int(input("Enter n: "))
total=0
for i in range(1,n+1):
 tatal+=i
 print("sum=",total)
 