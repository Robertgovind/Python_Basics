# Given a list in python and provided two indexes,Write a program to swap these two elements

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = int(input("Enter the size of the list: "))
list = []
for _ in range(n):
    num = int(input("Enter list item: "))
    list.append(num)
ind1 = int(input("Enter first index: "))
ind2 = int(input("Enter second index: "))

print("Before: ")
print(list)

temp = list[ind1]
list[ind1] = list[ind2]
list[ind2] = temp

print("After: ")
print(list)
