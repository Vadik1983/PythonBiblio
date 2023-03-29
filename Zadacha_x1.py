#*** (1)У вас есть массив чисел, составьте из них максимальное число. Например:

#[61, 228, 9] -> 961228

a = int(input("Введите количество элементов: "))

num = []
i = 0
for i in range(0, 1000, (1000 // a)):
    el = int(input("Введите число: "))
    num.append(el)
    print(num)

new_num = ""
for j in num:
    temp = str(num[j])
    new_num = new_num + temp
    print(new_num)