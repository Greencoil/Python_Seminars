# 18). Реализуйте алгоритм перемешивания списка.

import random

lenght = int(input('Введите длину списка: '))
list = [lenght]
for i in range(lenght - 1):
    list.append(random.randint(1, 9))

print(f'Cписок: {list}')

random.shuffle(list)
print(f'Перемешанный список: {list}')
