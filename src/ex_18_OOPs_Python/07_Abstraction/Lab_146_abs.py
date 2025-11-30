from abc import ABC,abstractmethod
class Father(ABC):
    def __init__(self,name):
        self.name=name

    @abstractmethod
    def loan(self):
        pass

class Child(Father):
    def loan(self):
      print("Giving 1L loan")


amit = Child("Amit")
amit.loan()


