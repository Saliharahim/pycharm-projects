strt=int(input("enter a number"))
stop=int(input("enter a number"))
def lit(a,b):
    l=[]
    for i in range(a,b+1,2):
       l.append(i)
    print(l)
lit(strt,stop)