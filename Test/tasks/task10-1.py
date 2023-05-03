people = ['Lis', 'Gas', 'Matras', 'Huivglas', 'Anton']
score = [2142, 3141, 4521, 1524, 1324]
direct = dict(zip(people, score))
direct['viga'] = 1346
direct.update(manager = 1422, bashik = 4365, dusher = 7124)
del direct['Anton']
del direct['Huivglas']
dawn = []
direct.pop('Lis')
print(direct)
print("Счёт удалённых" , dawn)