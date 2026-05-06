#
a={i:i*i for i in range (6)}
print(a)

##
b={i:i for i in range(10) if i%2==0}
print(b)

###
c="python"
d={char:c.count(char) for char in c}
print(d)

####
student=["Atharv","rutik","sarthak"]
word={name:name.upper() for name in student }
print(word)

#####
even = {i:i*i for i in range(10) if i%2==0}

print(even)