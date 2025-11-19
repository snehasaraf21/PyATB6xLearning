class Person:
    name = None
    age = None
    phone = None
    occupation = None

    def __init__(self):
        print("Enter the user inputs ,please share the name , age, phone_no, occupation ")
        self.name = input("Enter your name:\n ")
        self.age = input("Enter your age:\n ")
        self.phone = input("Enter your phone:\n ")
        self.occupation = input("Enter your occupation:\n ")

    def display_values(self):
        print("Name is ",self.name)
        print("Age is ",self.age)
        print("Phone is ",self.phone)
        print("Occupation is ",self.occupation)

Sneha = Person()
Sneha.display_values()