# Напишите функцию f, которая на вход принимает два числа a и b,
# и возводит число a в целую степень b с помощью рекурсии.
# Функция не должна ничего выводить, только возвращать значение

# a = 3; b = 5 -> 243 (3⁵)
# a = 2; b = 3 -> 8 

def f(a, b) -> int:
    if b <= 0:
        result = 1
    else:
        result = a
        result *= f(a,b-1)
    return result

a = int(input('Input your number: '))
b = int(input('Input desired positive degree: '))
print(f(a,b))