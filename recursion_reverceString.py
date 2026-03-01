def string(n):
    if n==0:
        return n
    return n[-1] + string(n[::6])
print(string("atharv"))