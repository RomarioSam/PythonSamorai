# Представьте, что у нас есть список целых чисел неограниченной вложенности.
# То есть наш список может состоять из списков, внутри которых также могут быть списки.
# Ваша задача превратить все это в линейный список при помощи функции flatten
#
# flatten([1, [2, 3, [4]], 5]) => [1, 2, 3, 4, 5]
# flatten([1, [2, 3], [[2], 5], 6]) => [1, 2, 3, 2, 5, 6]
# flatten([[[[9]]], [1, 2], [[8]]]) => [9, 1, 2, 8]
# Ваша задача только написать определение функции flatten


def flat(arr):
    list_ = []
    for i in arr:
        if not isinstance(i, list):
            list_.append(i)
            print(list_)
        else:
            list_ = list_ + flat(i)
    return list_

print(flat([1, [2, 3], [[2], 5], 6]))
print(flat([[[[9]]], [1, 2], [[8]]]))


import random

# first_m = [random.randint(1, 20) for i in range(int(input('Введите длину первого массива: ')))]
# second_m = [random.randint(1, 20) for i in range(int(input('Введите длину второго массива: ')))]
# print(first_m)
# print(second_m)
# print([el for el in first_m if el not in second_m])

def sum_delit(x):
    s = 0
    for i in range(1, x):
        if x % i == 0:
            s += i
    return s

k = int(input("Введите число: "))
for i in range(1, k + 1):
    if i == sum_delit(sum_delit(i)) and i != sum_delit(i) and i < sum_delit(i):
        print(f"{i} {sum_delit(i)}")