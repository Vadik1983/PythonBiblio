# задача 36: напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# аргументы num_rows и num_columns указывают число строк и столбцов таблицы, 
# которые должны быть распечатаны. нумерация строк и столбцов идет с единицы
# (подумайте, почему не с нуля). примечание: бинарной операцией называется любая операция,
# у которой ровно два аргумента, как, например, у операции умножения.

# *пример:*

# **ввод:** `print_operation_table(lambda x, y: x * y) ` 
# **вывод:**
# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36


num_rows = 6
num_columns = 6

def number(num_rows, num_columns):

    matrix = ([[(i + 1) * (j + 1) for j in range(num_columns)] for i in range(num_rows)])

    for i in matrix:
        print(*i, "\n")

    number = (x * y)
    print(number)


x = int(input("Введите номер строки: "))
y = int(input("Введите номер столбца: "))
number(num_rows, num_columns)
print(print_operation_table(lambda x, y: number(num_rows, num_columns)))
