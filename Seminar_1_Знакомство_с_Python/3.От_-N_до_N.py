# 3. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
n = abs(int(input('Введите число N: ')))

for i in range(-n, n + 1):
    print(i, end = ' ')