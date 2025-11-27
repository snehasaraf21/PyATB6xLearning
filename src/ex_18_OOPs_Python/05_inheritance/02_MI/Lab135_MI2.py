class Father1:
    def money(self):
        print("Father1 money is used")

class Father2:
        def money(self):
            print("Father2 money is used")

#class Son(Father1,Father2):#father1 here as its first
class Son(Father2, Father1):# MRO(method resolution order) whichever is first thats called#here father2

    def give_money(self):
        print("Son")
        self.money()

c = Son()
c.give_money()
