n=int(input("enter a number"))
st=len(str(n))
#print(st)
sum=0
temp=n
while temp>0:
    a=temp%10
    sum=sum+(a**st)
    temp//=10
if sum==n:
    print(sum,"is an armstrong number")
else:
    print(sum,"not armstrong")