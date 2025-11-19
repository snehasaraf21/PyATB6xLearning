print("Outside class1")


class MobilePhone:
    model = None

    def __init__(self):
        print("DC")#default constructor#it will be called first by default when yoy call the object


    def talk(self):
        print("MobilePhone talk")


iphone = MobilePhone()
iphone.talk()

print("Outside cLass 2")
