a = [1, 3, 7, 9, 13, 16, 19, 22]
i = 0
while i < len(a):
    if a[i] % 2 == 0:
        print(a[i], 'Чётное')
    elif a[i] % 2 != 0:
        print(a[i], 'Нечётное')
    i += 1