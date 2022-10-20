# 26. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример: o для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

fib = int(input('Введите число: '))
fib_num = []
for i in range(fib + 1):
    if i == 0:
        fib_num.append(i)
    elif i == 1:
        fib_num.append(i)
        fib_num.insert(0, i)
    else:
        fib_num.append(fib_num[len(fib_num)-1] + fib_num[len(fib_num) - 2])
        fib_num.insert(0, (-1) ** (i-1) * fib_num[len(fib_num) - 1])
print(f'Число Фибоначчи чила {fib}: ')
print(fib_num)