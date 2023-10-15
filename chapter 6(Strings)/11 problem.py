str = "The unexpected always happens"

print(str)
print(len(str))
print(str.find("pp"))
print(str[0:11])
print(str.replace("always", "never", 1))
new_string = "no matter what"
print(str + new_string)
# OR
print("{s1} {s2}".format(s1=str, s2=new_string))
