def calc(f):
    def add(a,b):
        a+b
        return result.calc(a,b)
    return add

#@calc
def sub(g,f):
    print("sub is",g-f)
sub(1,2)
# def mul(c,d):
#     print("mul is",c*d)
# mul(4,5)