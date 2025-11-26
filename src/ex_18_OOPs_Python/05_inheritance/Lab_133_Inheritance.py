#Single inheritance
#A subclass/child/son inherits from one Parent/base/father.

class baseTest:#parent class
    driver = "Chrome"
    def setup(self):

        print("Base setup with the browser and environment")

class LoginTest(baseTest):#child class which can access parent class
    def run(self):
        self.setup()
        print("Running the testcase-->"+ self.driver)

t = LoginTest()
t.run()


