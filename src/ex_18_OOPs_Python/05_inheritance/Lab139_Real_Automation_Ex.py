class BaseTest:
    def __init__(self,browser):
        self.browser = browser

    def setup(self):
        print(f"Launching {self.browser}")

class LoginTest(BaseTest):
    def run_test(self):
        self.setup()
        print("Running Login test")

class signUpTest(BaseTest):
    def run_test(self):
        self.setup()
        print("Running SignUp test")


t = LoginTest(browser="chrome")
t.run_test()

t = signUpTest("firefox")
t.run_test()