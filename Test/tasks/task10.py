a = ['Artem', 'Vova', 'Dasha', 'Masha', 'Eva', 'Sonya']
b = [19, 18, 0, 18]
ab = dict(zip(a, b))
# ab['Sonya'] = 10
ab.update(Sonya = 15, Eva = 10)
ab['Sonya'] = 17
del ab['Dasha']
z = ab.pop('Sonya')
ab2 = ab.copy()
ab.update(Dima = 3, Nik = 12)
for i in a:
    print(ab.get(i, 'ничего не найдено'))
print(ab, len(ab), ab2, len(ab2), z ,sep = '\n')
print('Sonya' not in ab)

for name in ab:
    print(name)