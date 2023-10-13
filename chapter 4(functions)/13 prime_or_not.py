def is_prime(n):
    for i in range(2, n + 1):
        if n % i == 0:
            return False
        else:
            return True


number = int(input("Enter the number: "))
result = is_prime(number)
if result == True:
    print("It is prime.")
else:
    print("It is not prime.")
