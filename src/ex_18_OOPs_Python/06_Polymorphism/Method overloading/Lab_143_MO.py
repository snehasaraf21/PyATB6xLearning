#Python does not support overloading traditionally

class MathClass:

    def add(self,a,b):#this is not used as it always uses the recent method or last method
        return a+b

    def add(self,a,b,c=10):#u can only overload in python by using default value
        return a+b+c

obj_ref = MathClass()
print(obj_ref.add(1,2))