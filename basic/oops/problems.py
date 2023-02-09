#  factorial using class

# class emp:
#     def fact(self,n):
#         f=1
#         for i in range(1,n+1):
#             f=f*i
#         return f
#
# obj=emp()
# n=int(input("enter the number"))
# f=obj.fact(n)
# print("factorial",f)

#  factorial using recursion

# class emp:
#     def fact(self,n):
#         if n==1:
#             return 1
#         else:
#             #return n*self.fact(n-1)
#             return n* emp.fact(self,n-1)
# obj=emp()
# n=int(input("enter the number"))
# f=obj.fact(n)
# print(f)

''' oops concept
1.encapsulation- wrapping up of data and function into a single unit..Eg- class
2.inheritence- To acquire the properties of  one class to another class
'''
# simple inheritence

# class a:
#     def display(self):
#         print('base class method')
# class b(a):
#     def displayb(self):
#         print("derived class method")
# obj=b()
# obj.display()
# obj.displayb()

# example:- sum of 2 numbers
# class a():
#     def read(self):
#         self.a=int(input("enter a number"))
#         self.b= int(input("enter a number"))
# class b(a):
#     def sum(self):
#         print("sum is:",self.a+self.b)
# obj=b()
# obj.read()
# obj.sum()

#multi level inheritence

# average
# class a():
#     def read(self):
#         self.a=int(input("enter a number"))
#         self.b= int(input("enter a number"))
# class b(a):
#     def sum(self):
#         self.s=self.a+self.b
#         return self.s
# class c(b):
#     def average(self):
#         print("average is",self.s/2)
# obj=c()
# obj.read()
# print("sum is",obj.sum())
# obj.average()

# heirarchical inheritence

# class a():
#     def read(self):
#         self.a=int(input("enter a number"))
#         self.b= int(input("enter a number"))
# class b(a):
#     def sum(self):
#         s=self.a+self.b
#         print("sum is:",s)
# class c(a):
#     def average(self):
#         print("average is",(self.a+self.b)/2)
# class d(a):
#     def product(self):
#         print("product is:",self.a*self.b)
# obj1=b()
# obj2=c()
# obj3=d()
# obj1.read()
# obj1.sum()
# obj2.read()
#obj2.average()
#obj3.read()
#obj3.product()

# multiple inheritence

class a():
    def personal_details(self):
        self.name=input("enter name")
        self.age= int(input("enter age"))
        self.place=input("enter your place")
class b():
    def salary_details(self):
        self.salary=int(input("enter salary"))
class c(a,b):
    def employee_details(self):
         employee_detail=self.name,self.age,self.place,self.salary
         print("employee_details :",employee_detail)
obj1=c()
obj1.personal_details()
obj1.salary_details()
obj1.employee_details()


