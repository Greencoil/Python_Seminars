# 15). Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

last_number = int(input('Введите число: '))
sum_number = 1

for i in range(last_number):
    sum_number *= i + 1
    print(sum_number, end = ' ')

print ()