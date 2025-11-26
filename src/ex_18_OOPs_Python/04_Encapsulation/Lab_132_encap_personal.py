class Home():

    def __init__(self):
        self.public_var = "father"
        self._protected_var = "brother"
        self.__private_var = "baby"

    def mom(self):
        print(self.public_var)
        print(self.__private_var)
        self.__wife()

    def __wife(self):
        print("private wife")

object_ref = Home()
#print(object_ref._protected_var)#technically accessible but not recommended
object_ref.mom()


