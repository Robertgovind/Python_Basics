# Leave all the numbers that are the multiple of 5 in the series
for i in range(1, 100):
    if i % 5 == 0:
        continue
    print(i, end=" ")
