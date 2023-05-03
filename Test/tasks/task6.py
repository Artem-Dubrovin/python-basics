x = ''
while len(x) < 5:
    y = input('ввод данных ')
    if y == "o":
        break
    x += y
print(x)