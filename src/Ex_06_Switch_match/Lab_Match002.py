from unittest import case

print("Enter which type of test you want to run")
test_type = input("Enter the test type : API , UI, Performance,secuirity \n")
match test_type:
    case "API":
        print("You are running a POSTMAN API testcase")
    case "UI":
        print("You are running a selenium testcase")
    case "Performance":
        print("You are running a performance testcase")
    case "secuirity":
        print("You are running a secuirity testcase")
    case _:
        print("please enter a valid test type")