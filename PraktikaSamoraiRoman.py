# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.



c = a = float(input("Первое: "))
d = b = float(input("Второе: "))
while b%1 != 0 or b < 1:
    b = float(input("Второе число должно быть целым и положительным! Повторите попытку: "))
d = b = int(b)


def pr(A, B, C, D):
    if B == 1:
        print(f"{A} в степени {D} = {C}")
        return
    C = C * A
    B -= 1
    pr(A, B, C, D)


pr(a, b, c, d)



# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.



X = float(input("Первое число: "))
while X%1 != 0 or X < 0: X = float(input("Число должно быть целое и неотрицательное! Повторите попытку: "))
Y = float(input("Второе число: "))
while Y%1 != 0 or Y < 0: Y = float(input("Число должно быть целое и неотрицательное! Повторите попытку: "))

def sum_(x, y):
    if y == 0:
        print(f"Сумма ваших чисел равна: {int(x)}")
        return
    x += 1
    y -= 1
    sum_(x, y)


sum_(X, Y)
