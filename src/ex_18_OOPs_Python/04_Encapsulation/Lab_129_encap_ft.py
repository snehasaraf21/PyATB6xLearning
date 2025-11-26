#encapsulation - hide the data members(class variables,instance variables)
#by using method


class car():
    def __init__(self):
        self.password = "sneha"#public variable-accesible everywhere
        self.__password_secure = "pass123"#private variable denoted by __,only avaible within the class

    def nanny(self):
            self.__password_secure = "345"


object_reference = car()
print(object_reference.password)
#print(object__reference.password) cant access as its a private variable

object_reference.nanny()

