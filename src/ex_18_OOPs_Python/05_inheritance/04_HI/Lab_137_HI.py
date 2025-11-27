class BaseTest:
    def setup(self):
        print("setup for BaseTest")

class LoginTest(BaseTest):
    def run(self):
        print("runnung Login Test")

class SignUpTest(BaseTest):
    def run(self):
        print("runnung Sign Up Test")

LoginTest().setup()
LoginTest().run()
SignUpTest().setup()
SignUpTest().run()

