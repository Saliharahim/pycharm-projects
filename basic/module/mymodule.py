l1=[]
def create():
    n=int(input("enter the number of elements"))
    for i in range(0,n):
        li=int(input("enter the values"))
        l1.append(li)
    print(l1)
# create()

#SEARCH ITEM

#l=[1,2,3,4,5]
def find():
    n=int(input("enter the number"))
    if n in l:
        print("present")
    else:
        print("not present")

#find()

# REMOVE

def remove():
    i = int(input("enter the value for remove"))
    if i in l:
        l.remove(i)
    else:
        print("not found")
    print(l)


# remove()

#  REPLACE

def replace():
    old = int(input("enter the item to replce"))
    new = int(input("enter the item to add"))
    for i in range(len(l)):
        if l[i] == old:
            l[i] = new
    print(l)
# replace()