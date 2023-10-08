number = int(input("Enter a number: "))

if number % 5 == 0 | number % 3 == 0:
    if number % 15 != 0:
        print("Required number")
else:
    print("Not Required number")
