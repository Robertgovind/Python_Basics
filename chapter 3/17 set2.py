names = {"Govind", "Ekisha", "Lalu", "Bablu", "Anjana"}

more_names = ["Tina", "Mina"]
names.update(more_names)
print(names)

names.remove("Tina")
print(names)

names.discard("Tina")
print(names)


s1={"ram","shyam"}
s2={"sita","ram","hari"}
s= s1.union(s2) 
print(s)

s=s1.intersection_update(s2)
print(s)

s=s1.symmetric_difference(s2)
print(s)