# Задача 32: Определить индексы элементов массива (списка), значения которых 
# принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

# Диапазон от 6 до 12

# Вывод: [1, 9, 13, 14, 19]
import random

def renge_num(N):
    numbers = []
    for i in range(N):
        temp = random.randint(-100, 100)
        numbers.append(temp)
    print(numbers)

    for j in range(N):
        if min <= numbers[j] <= max:
            print(numbers.index(numbers[j]), end= " ")


N = int(input('Введите число элементов: '))
min = int(input('Введите минимальное значение диапазона: '))
max = int(input('Введите максимальное значение диапазона: '))
renge_num(N)