# Nested list means a list inside a list

numbers = [4, 2, 6, 7, 5, 2, 3, 9, 0]
fruits = ["Orange", "Mango", "Apple", "Banana", "jack fruit"]

fruits.insert(2, ["Kiwi", "Papaya"])
print(fruits)
print(fruits[2][0])
print(fruits[2][1])
