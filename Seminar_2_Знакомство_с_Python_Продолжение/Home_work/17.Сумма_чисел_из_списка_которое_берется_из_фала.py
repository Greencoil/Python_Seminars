# 17). Задайте число N, создайте список: [-N, N]. Найдите произведение элементов на указанных позициях. Позиции (случайные) хранятся в файле file.txt (создаётся во время выполнения кода и зависит от количества элементов в списке) в одной строке одно число.
# Пример: N = 3 => [-3, -2, -1, 0, 1, 2, 3]

N = int(input('Введите число: '))
list = []

file = open("file.txt")
for i in range(-N, N + 1):
    list.append(i)

print(list)
result = 1

for line in file:
    print (list[int(line)], ' * ', end='' )
    result = result * list[int(line)]

print('= ', result)
