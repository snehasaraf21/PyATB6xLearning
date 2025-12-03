try:
    with open('testdata.txt', 'r') as file:
        print(file.read())
except FileNotFoundError as error:
     print(error)