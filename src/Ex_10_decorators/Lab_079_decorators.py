def add_secuirity(func):
    def wrapper():
        print("1.Before the function is called please check if you have following:")
        print("2.Helmet,License,knee guard,gloves")
        func()
        print("4.After calling the function is called please check if you have following")
        print("5.all the above is checked and returned")

    return wrapper()

@add_secuirity
def drive_ola_scooter():
    print("Driving ola scooter")

@add_secuirity
def drive_zypp_scooter():
    print("Driving zypp scooter")