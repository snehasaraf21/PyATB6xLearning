class car:
    name = None
    make = None
    model = None

    def __init__(self,o_name,o_make,o_model):#pc
        self.name = o_name
        self.make = o_make
        self.model = o_model

    def start_engine(self): #method
        print("Starting a car with the name:",self.name)
        print("Starting a car with the make:",self.make)
        print("Starting a car with the model:",self.model)


lambo= car(o_name="lambo",o_make="V6",o_model="2023")
lambo.start_engine()


bmw = car(o_name="bmw",o_make="1.5+Turbo",o_model="2022")
bmw.start_engine()

