colors = ("blue", "green", "yellow")
print(colors)

list = []
for i in reversed(colors):
    list.append(i)

rev_colors = tuple(list)
print(rev_colors)
