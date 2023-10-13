def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)


a = int(input("Enter a:"))
b = int(input("Enter b:"))
result = power(a, b)
print("a raise to the power b is: ", result)
