quetions=[
    [
        "which languge was used to create fb?","python","french","javascript","php","None",4
    ],
    [
        "which languge was used to create fb?","python","french","javascript","php","None",4
    ],
    [
        "which languge was used to create fb?","python","french","javascript","php","None",4
    ]
]

levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]

for i in range(0,len(quetions)):
    quetion=quetions[i]
    print(f"\n\n quetion for Rs.{levels[i]}")
    print(f"a.{quetion[1]}    b.{quetion[2]}")
    print(f"c.{quetion[3]}    d.{quetion[4]}")
    reply=int(input("Enter your ans: "))
    if(reply==quetion[-1]):
        print(f"correct ans you have won RS.{levels[i]}")
        if(i==4):
            money=1000
        elif(i==9):
            money=320000
        elif(i==14):
            money=10000000
        else:
            print("Wrong Answer!")
            break
        print(f"your take home money is{money[i]}")