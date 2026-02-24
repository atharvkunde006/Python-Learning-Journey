def large(num):
    i=100
    if (num>i):
        print(num,"is greater")
    else:
     print(i,"is greater")
num=150
large(num)

#reverse a string
def rev(string):
   print(string[::-1])
string="Atharv"
rev(string)

#count vowels in a string
def count(string):
   count=0
for i in string:
   if i in "aeiouAEIOU":
      count+=1
      print(count)
count(string)