# Zadacha_1
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

n = (input("Введите число: "))
numbers = ''
for i in n:
    if i.isdigit():
        numbers += i
sum = 0
for i in numbers:
    sum += int(i)
print(f'"Сумма всех цифр числа {n} равна -> " {sum}')