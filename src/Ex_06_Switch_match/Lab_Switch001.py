from unittest import case

day = int(input("Enter the day: \n"))
match day:
    case 1:
        print("Its Monday")
    case 2:
        print("Its Tuesday")
    case 3:
        print("Its Wednesday")
    case 4:
        print("Its Thursday")
    case 5:
        print("Its Friday")
    case 6:
        print("Its Saturday")
    case 7:
        print("Its Sunday")
    case _:
        print("please enter a valid day")

