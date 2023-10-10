names = {"Govind", "Ekisha", "Lalu", "Bablu", "Anjana"}
print(names)

print(len(names))

# Accessing items of sets
for i in names:
    print(i)

if "Govind" in names:
    print("Govind is in the set")

names.add("Riya")
print(names)

names.add("Riya")
print(names)
