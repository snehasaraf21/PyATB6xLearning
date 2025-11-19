class dog:
 #A
    name = None
    breed = None
    height = None
    weight = None

 #B
    def __init__(self,nameGiven,breedGiven):
        self.name = nameGiven
        self.breed = breedGiven

    def bark(self):
        print("Barking")
        print(self.name)



    def talk(self):
        print("Talking")

print("outside?")

chow = dog("chow","mistiff")
rancho = dog("rancho","desi")


chow.bark()
rancho.talk()
