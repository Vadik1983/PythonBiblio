# Дано 20+ значное целое число, проверить его на делимость на 7

# Ввод 234523642345789812354678654323454919865

# Вывод Делится

n = 234523642345789812354678654323454919865


def delim(n):
    num_1 = 0
    if n < 100:
        temp = n % 10
        num_1 = n // 10 - (temp * 2)
        if (num_1 % 7) == 0: print(True)
        else: print(False)
    else:
        return (delim(n // 10))
    

delim(n)

# def delim_1(n):
#     while n > 99:
#         res = (n // 10) - ((n % 10) * 2)
#         n //= 10
#     print(res)
#     if res % 7 == 0 : print (True)
#     else: print(False)

# delim_1(n)