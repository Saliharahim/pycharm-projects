#1. non parametrized constructor/default constructor

# class a:
#     def __init__(self):
#         print("non parametrized constructor")
# ob=a()

#2. parametrized constructor

# class a:
#     def __init__(self,name):
#         print("non parametrized constructor")
#         self.na=name
#     def display(self):
#         print("name is",self.na)
# ob=a("anu")
# ob.display()


# distructor
class a:
    def __init__(self,name):
        print("non parametrized constructor")
        self.na=name
    #def __del__(self):
        #print("distructor")
    def display(self):
        print("name is",self.na)
ob=a("anu")
del ob
ob.display()



