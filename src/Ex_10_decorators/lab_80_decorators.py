def before_after_ui_test(func):
    def wrapper():
        print("Before running the UI test")
        func()
        print("After running the UI test")

    return wrapper()


@before_after_ui_test
def test_ui():
    print("I am testing a UI test")