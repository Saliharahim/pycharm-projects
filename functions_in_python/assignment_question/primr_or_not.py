n=int(input("enter a number"))
def prime(num):
    f=1
    for i in range(2,(num//2)+1):
        if(n%i==0):
            f=0
            break
        else:
            continue
    if f==0:
            c="not prime"
    else:
            c="prime"
    return c
print(prime(n))


