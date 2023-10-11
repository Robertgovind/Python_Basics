phones = {
    "Govind": 9878787,
    "Rabin": 9787576,
    "Gita": 9876767,
    "Mina": 8767556,
}

# Using key
print(phones["Rabin"])
print(phones.get("Govind"))

print(phones.keys())

# Update values
phones["Govind"] = 9824803556

print(phones)

# Adding elements
phones["Sita"] = 343434
print(phones)

# Removing element
phones.pop("Rabin")

for i in phones:
    print(i)
    print(phones[i])

for i in phones.items():
    print(i)

for x, y in phones:
    print(x, y)
