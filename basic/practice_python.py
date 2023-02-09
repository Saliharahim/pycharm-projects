class Car:
    def __init__(self,name,price,colour):
        self.name=name
        self.price=price
        self.colour=colour
    def start(self):
        print(self.name,"engine started")
car1=Car("maruti",22,"red")
car2=Car("audi",44,"white")
car1.price=55
print(car1.name,car1.price)
print(car2.name)
car1.start()
