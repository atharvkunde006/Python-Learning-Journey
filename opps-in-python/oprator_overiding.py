class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
     return point(self.x+other.x,self.y+other.y)
s1=point(1,3)
s2=point(2,4)
s3=s1+s2
print(s3.x, s3.y)