#default argument
def name(fname,mname="Ashok",lname="kunde"):
    print("Hello",fname,lname)
    name("atharv")

#Kyeword Argument
def name(fname,mname,lname):
    print("Hello",fname,mname,lname)
    name(mname="peter",lname="weskwer",fname="jade")

#Required argument
def name(fname,mname,lname):
    print("hello",fname,mname,lname)
    name("atharv","rahul")

#variable lenghth Argument
def name(*name):
    print("Hello",name[0],name[1],name[2])
    name("atharv","ashok","kunde")

#keyword Arbitrary Argument
def name(**name):
    print("Hello",name["fname"],name["mname"])
    name(mname="ashok",lname="kunde",fname="Atharv")


#return statement
def name(fname,mname,lname):
    return"Hello","+fname+""+mname+""+lname
print(name("atharv","ashok","kunde"))
          