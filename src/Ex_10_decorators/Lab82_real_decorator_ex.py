import time


def print_logs(func):
    def wrapper():
        print("Start of the log")
        func()
        print("End of the log")

    return wrapper()

def time_decorator(func):
    def wrapper():
        start_time = time.time()
        print("Start time")
        func()
        end_time = time.time()
        print("End time")
        print("Total time : ", end_time - start_time)

    return wrapper

@time_decorator
@print_logs
def test_ui():
    print("Add a function,time taken by this function 1")
    time.sleep(2)


@time_decorator
@print_logs
def test_ui_2():
    print("Add a function,time taken by this function 2")
    time.sleep(5)
