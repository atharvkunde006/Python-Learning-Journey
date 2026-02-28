#
info={"cars",19,False,5.9,19}
print(info)

##
info={"cars",19,False,5.9,19}
for item in info:
    print(item)

### union and update method
cities={"nashik","delhi","pune","chennai"}
cities2={"nashik","nagpur","niphad","mumbai"}
cities3=cities.union(cities2)
print(cities3)

####symetric difference in set
cities={"nashik","delhi","pune","chennai"}
cities2={"nashik","nagpur","niphad","mumbai"}
cities3=cities.difference (cities2)
print(cities3)

#####difference and differnce update
ities={"nashik","delhi","pune","chennai"}
cities2={"nashik","nagpur","niphad","mumbai"}
cities3=cities.difference(cities2)
print(cities3)

###### intersection and intersection update
ities={"nashik","delhi","pune","chennai"}
cities2={"nashik","nagpur","niphad","mumbai"}
cities3=cities. intersection(cities2)