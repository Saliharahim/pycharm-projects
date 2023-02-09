def numb(n):
    if n>0:
        x = n + numb(n - 1)
        print(x)
    else:
        x=0
    return x
numb(5)

#factorial

