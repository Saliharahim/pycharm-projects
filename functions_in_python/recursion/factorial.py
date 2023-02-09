def num(n):
    if n==1:
        return n
    else:
        x=n*num(n-1)
        print(x)
print(num(5))