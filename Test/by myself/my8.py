# Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True, 
# если оно простое, и False - иначе.

def is_prime(a):
    count = 0
    for i in range(1, a + 1):
        if a % i == 0:
            count += 1
        if count > 2:
            return False
    return True
print(is_prime())