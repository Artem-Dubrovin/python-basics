import os
flag = True
count = 0
x = 5
while flag:
    count += 1
    sayt = input("Введите домен\n")
    if count == x:
        flag = False
    if sayt == 'завершить':
        break
    if 'https://' in sayt:
        os.system('start ' + sayt)
    elif 'www.' in sayt:
        sayt = 'https://' + sayt
        os.system('start ' + sayt)
    else:
        sayt = 'https://www.' + sayt
        os.system('start ' + sayt)