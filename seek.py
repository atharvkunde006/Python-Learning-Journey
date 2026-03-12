file=open("code.txt" ,"r")
file.seek(8)
print(file.read())
file.close()