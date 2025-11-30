class MathOperation:
    @staticmethod
    def add(a,b):#static
        return a+b
    def div(selfself,a,b):#non static
        return a/b
    def sub(self,a,b):
        return a-b

#we can directly access static method but for non static we need to create a object ref

print(MathOperation.add(4,4))

t=MathOperation()
print(t.div(4,4))
print(t.sub(4,4))