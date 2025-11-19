a=10 # this is a global variable ,can be used anywhere in program
class Person:
      b =11 # instance variable can be used only in class

      def print_info(self):
          c=20
          print(c)#local to this method or function
          print(self.b)#insyance variable
          print(a)#global

object_ref = Person()


