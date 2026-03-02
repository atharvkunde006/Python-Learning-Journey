text="programmer"
a={}
for ch in text:
    if ch in a:
        a[ch]+=1
    else:
        a[ch]=1
    print(a)