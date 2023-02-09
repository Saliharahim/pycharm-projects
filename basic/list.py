l=[]
def create():
    n=int(input("enter the number of elements"))
    for i in range(0,n):
        li=input("enter the values")
        l.append(li)
    print(l)
# create()

#SEARCH ITEM

l=[1,2,3,4,5]
def search():
    n=int(input("enter the number"))
    if n in l:
        print("present")
    else:
        print("not present")

#find()

# REMOVE

def remove():
    i=int(input("enter the value for remove"))
    if i in l:
        l.remove(i)
    else:
        print("not found")
    print(l)
# remove()

#  REPLACE

def replace():
    old=int(input("enter the item to replce"))
    new=int(input("enter the item to add"))
    for i in range(len(l)):
        if l[i]==old:
            l[i]=new
    print(l)
#replace()

while True:
    opt=int(input("enter the option\n1.create\n2.search\n3.remove\n4.replace"))
    if opt==1:
        create()
    elif opt==2:
        search()
    elif opt==3:
        remove()
    elif opt==4:
        replace()
    else:
        print("invalid option")
    break

