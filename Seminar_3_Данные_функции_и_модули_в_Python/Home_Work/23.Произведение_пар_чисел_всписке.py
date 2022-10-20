# 23. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: o [2, 3, 4, 5, 6] => [12, 15, 16]; o [2, 3, 5, 6] => [12, 15]

size = int(input('Введите размер списка '))
numbers = []


for i in range(size):
    digits = int(input(f'Введите число {i + 1} '))
    numbers.append(digits)
print(numbers)

for i in range(len(numbers)):
    while i < len(numbers)/2 and size > len(numbers)/2:
        size -= 1
        comp = numbers[i] * numbers[size]
        i += 1 
        print(f'Сумма произведения чисел расположенных на {i} и {size} поциях списка равна: {comp}')   

