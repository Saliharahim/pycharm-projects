import mymodule


while True:
    opt=int(input("enter the option\n1.create\n2.search\n3.remove\n4.replace"))
    if opt==1:
        mymodule.create()
    elif opt==2:
        mymodule.search()
    elif opt==3:
        mymodule.remove()
    elif opt==4:
        mymodule.replace()
    else:
        print("invalid option")
    break
