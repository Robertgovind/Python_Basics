# List comprehension is the process of making new list from the items of existing list

numbers = [4, 2, 6, 7, 5, 2, 3, 9, 0]
fruits = ["Orange", "Mango", "Apple", "Banana", "jack fruit"]

new_numbers = [num for num in numbers if num > 5]
print(new_numbers)

new_fruits = [fruit for fruit in fruits if "a" in fruit]
print(new_fruits)

# copying a list
new_fruits = fruits.copy()
print(new_fruits)

# Concatinate
new_list = fruits + numbers
print(new_list)
