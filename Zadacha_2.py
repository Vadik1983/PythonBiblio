234#Задача 2: Найдите сумму цифр трехзначного числа.

number = int(input('Введите число: '))
sum = 0
if number < 0 : number = number *(-1)
while number > 0:
    digit = (number % 10)
    sum = sum + digit
    number = number // 10
print(sum)

# Это решение подходит для любого целого числа.