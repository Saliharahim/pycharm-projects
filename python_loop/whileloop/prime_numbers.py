n=int(input("enter a number"))
p=0
i=2
while i<n:
    if n%i==0:
        p=1
    print("not prime number")
    i=i+1


    if p==0:
        print(" prime")

