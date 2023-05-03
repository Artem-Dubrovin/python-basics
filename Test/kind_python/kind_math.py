a = abs(-5) #функция всегда вызывается с числовым аргументом. (Модуль)
b = min(1, 2, -4, 7, -3, 5) #Вызывает минимальное значение.
c = max(2, 4, -6, 23) #Вызывает максимальное значение.
d = pow(9, 1/2) #Степень, корень "6 ** 2"
e = round(0.5) #Округляет (Можно округлять до сотых, тысячных round(7.34523, 2) = 7.35, round(283.5315, -2) = 300.0) 
print(d)

import math
math.ceil(5.2)
math.floor(7.1)
math.factorial(3)
math.trunc(3.65)
math.log2(4)
math.log10(1000)
math.sqrt(49)
math.sin()
math.cos()
math.pi
math.e

a, b = map(float, input("Введите две стороны прямоугольника: ").split())
print("Периметр: ", 2 * (a + b))