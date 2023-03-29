# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X
# в массиве A[1..N]. Пользователь в первой строке вводит натуральное число
# N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X

import random

N = int(input('Введите число N: '))


def count(N):
    numbers = []
    for i in range(N):
        temp = random.randint(0, 10)
        numbers.append(temp)
    print(numbers)

    X = int(input('Введите число X: '))
    count = 0
    j = 0
    while j < len(numbers):
        if numbers[j] == X:
            count += 1
        j += 1
    print(f'Число Х встречается {count} раз')

count(N)