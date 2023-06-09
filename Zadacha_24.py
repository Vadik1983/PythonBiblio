# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод 
# – на i-ом кусте выросло ai ягод. В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход,
# находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.

import random

def max_berry(N):
    berrys = []
    sum_berr = []
    for i in range(N):
        berr = random.randint(0, 10)
        berrys.append(berr)
    print(berrys)

    j = 0
    while j < (len(berrys) - 2):
        sum = berrys[j] + berrys[j + 1] + berrys [j + 2]
        sum_berr.append(sum)
        j += 1
    
    sum1 = berrys[0] + berrys[1] + berrys[-1]
    sum_berr.append(sum1)

    sum2 = berrys[0] + berrys[-1] + berrys[-2]
    sum_berr.append(sum2)

    print(sum_berr)

    print(max(sum_berr))

N = int(input("Введите количество кустов: "))
max_berry(N)


# Эталонное решение
# n = int(input())
# arr = list()
# for i in range(n):
#     x = int(input())
#     arr.append(x)

# arr_count = list()
# for i in range(len(arr) - 1):
#     arr_count.append(arr[i - 1] + arr[i] + arr [i + 1])
# arr_count.append(arr[-2] + arr[-1] + arr[0])
# print(max(arr_count))