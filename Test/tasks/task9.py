n = list(range(1,21))
b = n.copy()
m = []
for i in n:
    if i % 2 == 0:
        m.append(i)
        n.remove(i)
print(m)
print(n)
print(b)