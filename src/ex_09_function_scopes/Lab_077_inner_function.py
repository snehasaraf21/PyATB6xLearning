def outer_function():
    var1 = 30

    def inner_function():
        var2 = 20
        print(var1)

    def inner_function2():
            var3 = 30
            print(var1)

    inner_function()
    inner_function2()


outer_function()