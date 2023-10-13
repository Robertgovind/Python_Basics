def sum(n):
    if n == 1:
        return 1
    return n + sum(n - 1)


number = int(input("Enter the number: "))
sum = sum(number)
print("The sum is: ", sum)
