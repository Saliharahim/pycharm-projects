# def display_person(*args):
#     for i in args:
#         print(i)
#
#
# display_person(name="Emma", age="25")

def display(**kwargs):
    for i in kwargs:
        print(kwargs[i])

display(emp="Kelly", salary=9000)