
def make_adder():
    x=5
    def adder():
        y=2
        s=x+y
        return s
    return adder

a = make_adder()
print(a())
