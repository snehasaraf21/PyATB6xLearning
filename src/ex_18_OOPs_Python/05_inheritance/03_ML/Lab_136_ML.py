class TestSuite:
    def info(self):
        print("This is GF-->Step1")

class BaseTest(TestSuite):
    def setup(self):
        print("This is F-->Step2")

class UITest(BaseTest):
    def run(self):
        self.info()
        self.setup()
        print("This is S-->Step3")

test = UITest()
test.run()
