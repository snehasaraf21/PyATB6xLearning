class BaseTest:
    def setUp(self):
        print("Base Setup")

    def run(self):
        print("Base Run")

class LoginTest(BaseTest):
    def run(self):#override
        print("Login Test")

class signUpTest(BaseTest):
        def run(self):#override previous metod thts run
        print("Sign Up")

t = signUpTest()
t.run()

