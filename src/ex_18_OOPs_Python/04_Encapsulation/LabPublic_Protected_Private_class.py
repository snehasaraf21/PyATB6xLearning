class TestExample:
    def __init__(self):
        self.driver = "Chrome"#public variable
        self._config = "STAG"#protected
        self.__api__key = "ABC123"#private


    def show(self):
        print(f"Driver: {self.driver}")
        print(f"Config: {self._config}")#only accesible through show method as its protected varibale and is encapsulated within the class
        print(f"APIKey: {self.__api__key}")


obj = TestExample()
obj.show()

#accessible level
#print(obj.driver)#public-accessible
#print(obj._config)#protected - accessible but not recommended
#print(obj.__api_key)#private nt accessible gives error
#print(obj._TestExample__api__key)#accesible via name mangaling