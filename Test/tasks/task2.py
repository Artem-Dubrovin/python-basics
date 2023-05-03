x = input("ввдедите число ")
if '.' in x:
    x = float(x)
elif 'f' in x:
    print('недопустимый тип данных')
else:
    x = int(x)

if x == 0:
    print('x равен НУЛЮ')
elif type(x) == type(1) or type(x) == type(1.1):
    print('x допустимое значение')
else:
    print('x недопустимый тип данных')