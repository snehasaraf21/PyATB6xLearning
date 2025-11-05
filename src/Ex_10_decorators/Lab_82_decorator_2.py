def decorator1(func):
    def wrapper():
        print("This is a decorator1")
        func()
    return wrapper()

def decorator2(func):
    def wrapper():
        print("This is a decorator2")
        func()
    return wrapper


@decorator1
@decorator2
def say_hello():
    print("Hello World")