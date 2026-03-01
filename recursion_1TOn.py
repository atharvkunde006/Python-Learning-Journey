def sum (n):
    if n==0:
        return
    sum(n-1)
    print(n)
sum(3)