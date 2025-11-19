class dog:
 #A
    name = None
    breed = None
    height = None
    weight = None

 #B
    def bark(self):
        print("Barking")
        print(self.name)

    def talk(self):
        print("Talking")

print("outside?")

chow = dog()
ranchow = dog()
#chow is the object reference and dog() is a object
