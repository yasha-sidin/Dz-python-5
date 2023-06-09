# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
#
# *Пример:*
#
# 2 2
#     4

def Sum(a, b):
    if (a == 0 and b == 0):
        return 0
    if (a < 0 or b < 0):
        return None
    if (a < b):
        return Sum(a, b - 1) + 1
    if (a == b):
        return Sum(a - 1, b - 1) + 1 + 1
    if (b < a):
        return Sum(a - 1, b) + 1

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
print(f"Sum of {a} and {b} = {Sum(a, b)}")