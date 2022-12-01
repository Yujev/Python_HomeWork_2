# Задача_2
# Задайте список из n чисел последовательности (1 + 1/n)^n.  Вывести в консоль сам список и сумму его элементов.

from msilib import sequence

list = int(input("Введи число: \n"))

def get_squerence(list):
    return [round((1 + 1 / i) ** i, 3) for i in range(1, list + 1)]
s = get_squerence(list)

print("Твой список: ")
print(s)
print('Сумма элементов списка равна:')
print(round(sum(s), 3))

