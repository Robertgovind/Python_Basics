def print_num(n):
    if n == 0:
        return
    print_num(n - 1)
    print(n)


number = int(input("Enter the number: "))
print_num(number)
