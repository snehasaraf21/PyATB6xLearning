class calc():
    a = None
    b = None

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a+self.b

    def sub(self):
        return self.a-self.b

    def mul(self):
        return self.a*self.b

    def div(self):
        return self.a/self.b

object_ref = calc(10,10)
print("Sum :",object_ref.sum())
print("Sub:",object_ref.sub())
print("Multiplication:",object_ref.mul())
print("Division",object_ref.div())