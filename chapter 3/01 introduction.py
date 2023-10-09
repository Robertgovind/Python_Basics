# Lists are used to store multiple items in a single variable
# Lists are created using square brackets

fruits = ["Orange", "Mango", "Apple", "Banana", "jack fruit"]

# List items are
# Indexed
# Ordered
# Mutable
# Duplicates allowed
# Any datatype
# Mix of different data types

fruits = ["Orange", "Mango", "Apple", "Banana", "jack fruit"]
print(fruits)
print(type(fruits))
print(len(fruits))

if "Mango" in fruits:
    print("Mango is included in the list")
if "Mango" not in fruits:
    print("Item is not included")   