def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


number = int(input("Enter the number: "))
result = factorial(number)
print("The factorial is:", result)
