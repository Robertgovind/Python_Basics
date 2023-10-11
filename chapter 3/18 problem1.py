# Given three arrays, We have to find common elements in three arays.
arr1 = [1, 2, 3, 4, 5, 6, 7, 8]
arr2 = [3, 4, 5, 6, 6, 8]
arr3 = [5, 7, 3, 9, 0]

s1 = set(arr1)
s2 = set(arr2)
s3 = set(arr3)

s = s1.intersection(s2)
print(s)

final = s.intersection(s3)
print("Final: ")
print(list(final))
