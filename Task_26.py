# Задача 26:  Посчитать факториал (произведение 1 до N) и треугольное число (сумма чисел от 1 до N)
# для числа N ЧЕРЕЗ РЕКУРСИЮ и без циклов

def Factorial(number):
    if (number == 0):
        return 1
    return number * Factorial(number - 1)

def TriangleNumber(number):
    if (number == 0):
        return 0
    return number + TriangleNumber(number - 1)

number = int(input("Введите число: "))
print(f"Factorial = {Factorial(number)}")
print(f"Triangle number = {TriangleNumber(number)}")