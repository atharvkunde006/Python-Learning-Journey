# update
info={'name':'Atharv','age':20,'eligible':True}
info.update({'name':'sarthak'})
print(info)

## clear
a={'name':'Atharv','age':20,'eligible':'True'}
a.clear()
print(a)

### pop
a={'name':'atharv','age':20,'eligible':'True'}
a.pop("name")
print(a)

#### popitem
a={'name':'Atharv','age':20,'eligible':'True'}
a.popitem()
print(a)

##### del
a={'name':'Atharv','age':20,'eligible':'True'}
del a ['age']
print(a)