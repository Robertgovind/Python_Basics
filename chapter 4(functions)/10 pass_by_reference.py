# Modify provides the reference to the original variable
def modify(list):
    list.append("Rohit")
    print("Inside function: ")
    print(list)


list = ["Govind", "Ram", "Shyam", "Hari"]
modify(list)

print("Outside function: ")
print(list)
