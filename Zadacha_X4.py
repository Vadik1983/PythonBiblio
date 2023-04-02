# У вас есть массив чисел, составьте из него максимальное число. Например:
#  [61, 228, 9] -> 961228

import random
a = []
for x in range(random.randint(3, 6)):
    a.append(random.randint(1, 250))
print(a)

s = sorted(map(str, a), reverse = True)
# print(s)
n = ''
for i in s:
    n = n + i
print('искомое чимло: ' + n)

# Решение преподавателя:

# join_to_biggest = lambda a: int(''.join(sorted(map(str, a), reverse = True)))
# if __name__ == '__main__':
#     print(join_to_biggest([501, 2, 1, 80, 9]))

