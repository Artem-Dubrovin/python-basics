# Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, 
# если год високосный, и False иначе.

def is_year_leap(year):
    if year % 4 == 0:
        return 'Високосный'
    else:
        return 'Не високосный' 
a = int(input('Введите год: '))
print(is_year_leap(a))
b = 'aaaaaaaaaaaaaa'
print(dir(b))