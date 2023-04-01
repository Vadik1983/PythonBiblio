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


    print(result)

a = int(input('Введите каличество элементов первого набора чисел: '))
b = int(input('Введите каличество элементов второго набора чисел: '))
numbers(a, b)


# Эталонное решение
# mol = [int(x) for x in input().split()]
# n = mol[0]
# m = mol[1]
# set_1 = set()
# set_2 = set()
# list_1 = list()
# a = [int(x) for x in input().split()]
# k = set(a)
# for i in k:
#     set_1.add(i)
# b = [int(x) for x in input().split()]
# k1 = set(b)
# for i in k1:
#     set_2.add(i)
# lok = set_1 & set_2
# kool = list(lok)
# kool.sort()
# for i in kool:
#     print(i, end=' ')
