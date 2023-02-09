def upper(fun):
    def wrapper():
        result=fun()
        return result.upper()
    return wrapper()
def hello():
    return "hello"
f=upper(hello)
print(f)