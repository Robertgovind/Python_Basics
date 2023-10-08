cost_price = float(input("Enter the const price: "))
selling_price = float(input("Enter the selling price: "))

if selling_price > cost_price:
    print("Profit")
    print("Profit Amount: ", selling_price - cost_price)
elif cost_price > selling_price:
    print("Loss")
    print("Loss Amount: ", cost_price - selling_price)
else:
    print("Neither loss nor profit")
