# 22. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: o [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

size = int(input('Введите размер списка '))
numbers = []
avg = 0
for i in range(size):
    digits = int(input(f'Введите число {i + 1} '))
    numbers.append(digits)
    if i % 2 != 0:
        avg += numbers[i]


print(numbers)
print(f'Сумма чисел на нечетных позициях равна {avg}')