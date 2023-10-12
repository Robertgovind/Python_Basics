# Kekyworded arguments
def details(**kwargs):
    for x, y in kwargs:
        print(x, y)
    return


details(name="Govind", age="23", roll="paso78bei015", address="Kalyanpyr-09")
