# 6. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
s = int(input('Введите число недели: '))
if s > 0 and s < 8:
    if s == 6 or s == 7:
        print('Да, это выходной день')
    else:
        print('Нет, это рабочий день')
else:
    print('Неверное число')