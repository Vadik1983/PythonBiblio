# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине
# элемент к заданному числу X. Пользователь в первой строке вводит натуральное
# число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X

import random

N = int(input('Введите число N: '))

def close_number(N):
    numbers = []
    for i in range(N):
        temp = random.randint(0, 10)
        numbers.append(temp)
    print(numbers)

    X = int(input('Введите число X: '))
    if X in numbers:
        numbers_1 = sorted(numbers)
        j = numbers_1.index(X)
        a = numbers_1[j - 1]
        b = numbers_1[j + 1]

        if (b - X) < (X - a):
            print(f"Ближайшее число: {b}")
        elif (b - X) < (X - a):
            print(f"Ближайшее число: {a}")
        else:
            print(f"Ближайшие числа: {a} и {b}")
    else:
        print("Этого числа нет в массиве")

close_number(N)