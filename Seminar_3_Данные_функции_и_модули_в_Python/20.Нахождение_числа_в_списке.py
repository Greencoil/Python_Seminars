# 20. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
from cgi import test


find_number = int(input('Введите искомое число: '))
list_1 = ['qer4321', '5yk2w4r', '568u3jy7', '391kfs', '95674lhs']
count = 0
for i in list_1:
    if str(find_number) in i:
        count += 1
if count > 0:
    print(f'Ура, ура число {find_number} есть в списке')
else:
    print(f'К сожалению, число {find_number} отсутствует с писке')