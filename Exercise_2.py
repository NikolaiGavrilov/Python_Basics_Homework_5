# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# Функция не должна ничего выводить, только возвращать значение.

# Пример:

# sum(2, 2)
# # 4

def sum(a, b) -> int:
    if b == 0:
        return a
    if b > 0:
        return sum(a+1, b-1)
    elif b < 0:
        return sum(a-1, b+1)

a = int(input('Input your first number: '))
b = int(input('Input your second number: '))
print(sum(a, b))