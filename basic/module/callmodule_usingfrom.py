from mymodule import *
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
