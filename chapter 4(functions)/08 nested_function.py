def outer_function():
    a = 4

    def inner_function():
        y = 8
        return a + y

    return inner_function()


print("The sum is: ", outer_function())
