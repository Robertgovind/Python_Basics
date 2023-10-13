def print_num(n):
    if n == 0:
        return
    print(n)
    print_num(n - 1)


number = int(input("Enter the number: "))
print_num(number)
