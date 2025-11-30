class o:
    @staticmethod
    def sum(a,b):
        return a+b
    @staticmethod
    def sub(a,b):
        return a-b
    @staticmethod
    def mul(a,b):
        return a*b

print(o.sum(4,2))#we can directly access static method we dont have to create a object
print(o.sub(4,2))
print(o.mul(4,2))