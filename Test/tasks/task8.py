# m = [[4, 5], [6, 7], ['python', 10]]
# m += m
# print(m)

# m = list()
# n = list(range(15))
# for i in n:
#     if i == 8:
#         continue
#     m += [i]
# print(m)

# n = 'mouse'
# n[1] = 'a'   #str неизменяемый тип данных
# print(n[1])

#Методы: append, insert, count, sort, reverse, pop, remove, clear, extend, copy

x = list(range(10))
z = x.copy()
print(x)
# x.append(4) #добавляет в конец то, что в скобках
# x.insert(2, 59) #добавляет по индексу
# print(x.count(9)) #считает сколько значений, указанное в скобках
# x.sort(reverse = True) #сортирует
x.reverse() #разворачивает
y = x.pop(3) #удаляет по индексу с сохранением элемента в значении 
x.remove(9) #удаляет
# x.clear() #очищает
# x.extend([5]) #добавляет в список элементы
# x.copy()
print(x, y)
print(z)