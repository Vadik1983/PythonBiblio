# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
import random

n = int(input("Введите количество монет: "))

def avers_revers(n):
    money = []
    for i in range(n):
        m = (random.randint(0, 1))
        money.append(m)
    print(money)

    count = 0
    count1 = 0

    j = 0
    while j < len(money):
        if money[j] == 1:
            count += 1
        else:
            count1 += 1
        j += 1
    if count1 <= count:
        print(count1)
    else:
        print(count)
avers_revers(n)