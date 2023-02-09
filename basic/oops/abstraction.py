from abc import ABC,abstractmethod
#abstract class
class polygon(ABC):
    #abstract method
    @abstractmethod
    def sides(self):
        pass
    def display(self):
        print("non abstract method")
class triangle(polygon):
    def sides(self):
        print("triangle has 3 sides")

t=triangle()
t.sides()
t.display()

