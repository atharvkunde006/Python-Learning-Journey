# first program
a=9
b=8
gmean=(a*b)/(a+b)
print(gmean)
c=8
d=7
gmean2=(c*d)/(c+d)
print(gmean2)

# second program
def CalculateGmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)
    a=9
    b=8
    if(a>b):
        print("first number is greater")
    else:
        print("Second number is greater or equal")
        CalculateGmean(a,b)
        c=8
        d=74
        
# third program
def CalculateGmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)
    def isGreater(a,b):
        if(a>b):
         print("first number is grater")
        else:
         print ("second number is greater")
         def isLesser(a,b):
            pass
         a=9
         b=8
        isGreater(a,b)
        CalculateGmean(a,b)
