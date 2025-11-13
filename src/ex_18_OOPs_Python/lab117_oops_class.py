class Person: # class should be ideally start with upper case
    #attribute
    name = None
    age = None
    id = None
    email = None
    height = None
    weight = None
    gender = None
    phone_no = None
    address = None



    #behaviour
def talk(self):#self is a first argument
     print("I can talk")#no argument no return


def sleep(selp,name):#argument with no return
    print("I am a method")
    return None


def walk(self):#arg without return
    print("I am walking")

def walk_return(self):#no arg  with return
    return "I am walking again"

#function inside class is a method and outside its called as function
#create object of a class
#objectref = class()-->object
sneha = Person()#where person() is called object
amit = Person()
vedant = Person()#u can create multiple
print(sneha.name)  # attribute
sneha.walk("Amit")