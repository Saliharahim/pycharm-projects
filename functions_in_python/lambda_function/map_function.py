def  mp(a,b):
    return a+ b
x=map(mp,("apple","grapes","banana"),("berry","cherry","friuts"))
print(list(x))


#using lammbda

# y=map(lambda a,b:a+b,(1,2,3),(4,3,4))
# print(list(y))


l1=[1,2,3,4,5,6]

f= map(lambda n:n*2,l1)
print(list(f))