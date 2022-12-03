# Задача_3
# Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод

import random
list = int(input("Введи размер списка:\n "))

First_list = []
for i in range(list):
    First_list.append(i)

Second_list = First_list[:]
for i in range(len(Second_list)):
    n = random.randint(0, len(First_list)-1)
       if First_list[n - 1] != First_list[n]:
        Second_list.append([n])
print(f'Изначальный и [смешанный] списки: {Second_list}')


