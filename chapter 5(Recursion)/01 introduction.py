def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)


number = int(input("Enter the number: "))
result = factorial(number)
print("The factorial is : ", result)
