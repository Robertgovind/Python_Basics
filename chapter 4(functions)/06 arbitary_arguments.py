def sum_all(**args):
    sum = 0
    for i in args:
        sum += i
    return sum


sum = sum(3, 4, 2, 5, 6, 7, 3)
print("The sum is: ", sum)
