# # Цикл While

# s = 0
# i = 1
# N = 1000
# while i <= N:
#     s += i
#     i += 1
# print(s)

# pass_true = "123"
# ps = ''
# while ps != pass_true:
#     ps = input("Введите пароль: ")
# print('Вход в систему')

a = int(input("Введите число: "))
i = 1
while i <= a:
    if i % 15 == 0:
        print (i)
    i += 1