a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))

try:
    div = a / b

except TypeError:
    print("Can not be divided.")

finally:
    print("Can be divided and the reslut is : ", div)
