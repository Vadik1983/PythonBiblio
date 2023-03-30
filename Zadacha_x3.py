# Сравнение двух массивов

import random

def array_1(n, m):
    array_1 = []
    for i in range(n):
        arr1 = random.randint(0, 10)
        array_1.append(arr1)
    print(array_1)

    array_2 =[]
    for i in range(m):
        arr2 = random.randint(0, 10)
        array_2.append(arr2)
    print(array_2)

    array_result = []
    for i in array_1:
        if i not in array_2:
            array_result.append(i)
    print(array_result)
    
n = int(input("Введите количество элементов первой последовательности: "))
m = int(input("Введите количество элементов второй последовательности: "))

array_1(n, m)

