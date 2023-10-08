number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

if number1>number2:
    if number1>number3:
        print("Greatest: ",number1)
    else:
        print("Greatest: ",number3)
else:
    if number2>number3:
        print("Greatest: ",number2)
    else:
        print("Greatest: ",number3)
