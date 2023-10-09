# Stop the series when first multiple of 20 occurs
for i in range(1, 100):
    if i % 20 == 0:
        break
    print(i, end=" ")
