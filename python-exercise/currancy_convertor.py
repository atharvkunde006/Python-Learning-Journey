with open ('currancy_data.txt') as f:
    lines=f.readlines()
    currancyDict={}
    for line in lines:
     parsed=line.split("\t")
currancyDict[parsed[0]]=parsed[1]
amount=int(input("Enter amount:\n"))
print("Enter the name of currancy you want to convert this amount to ? available options:/n")
[print (item) for item in currancyDict.keys()]
currancy=input("please enter one of this values:\n")
print(f"{amount} INR is equal to {amount *float(currancyDict [currancy])} {currancy}")