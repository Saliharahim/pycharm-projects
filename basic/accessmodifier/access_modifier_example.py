# prgm to illustrate access modifier of a class

#super class
class a:
    # public data member
    var1=None

    #protected
    _var2= None

    #private data
    __var3=None

    #constructor
    def __init__(self,var1,var2,var3):
        self.var1=var1
        self._var2=var2
        self.__var3=var3

        #public member function
    def displaypublicmemb(self):
        #accessing public data members
        print("public data member:",self.var1)

    #protected member function
    def _displayprotectedmemb(self):
        # accessing protected data members
        print("protected data member:", self._var2)

    # private member function
    def __displayprivatememb(self):
        # accessing private data members
        print("private data member:", self.__var3)

    # public member function
    def accessprivatememb(self):
        #access private member function
        self.__displayprivatememb()

# derived class
class b(a):
    #constructor
    def __init__(self,var1,var2,var3):
        a.__init__(self,var1,var2,var3)

    #public member function
    def accessprotectedmemb(self):
        #accessing protected member function of super class
        self._displayprotectedmemb()

# creating objects of the derived classx
obj=b("pub_red","pro_white","private_green")

#calling public member functions of the class
obj.displaypublicmemb()
obj.accessprotectedmemb()
obj.accessprivatememb()
#object can access public member
print("object is accessing public member:",obj.var1)
#object can access protected member
print("object is accessing protected member",obj._var2)
#object can not access private member,so it will generate attribute error
#print(obj.__var3)
print(obj._a__var3)#acessing name manglede variables
''' Aprocess in which any given identifier with one trailing underscore and 2 leading underscores
is textually replaced with the _classname__identifier is known as name mangling
In _classname__identifier name, classname is the name of current class where identifier is present'''


