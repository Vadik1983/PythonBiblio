# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.
import random


def numbers(a, b):
    arr_a = []
    arr_b = []
    result = []

    for i in range(a):
        x = random.randint(0, 10)
        arr_a.append(x)
    print(arr_a)
    
    for i in range(b):
        y = random.randint(0, 10)
        arr_b.append(y)
    print(arr_b)

    x = set(arr_a)
    y = set(arr_b)
    result = x.intersection(y)

    # j = 0
    # k = 0
    # while j < len(arr_a):
    #     while k < len(arr_b):
    #         if arr_b[k] == arr_a[j]:
    #             result.append(arr_b[k])
    #             k += 1
    #         else:
    #             k += 1
    #     j = j + 1

    print(result)

a = int(input('Введите каличество элементов первого набора чисел: '))
b = int(input('Введите каличество элементов второго набора чисел: '))
numbers(a, b)