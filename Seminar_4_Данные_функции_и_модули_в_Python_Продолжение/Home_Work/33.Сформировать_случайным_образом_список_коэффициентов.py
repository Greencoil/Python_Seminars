# 33). Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k и приравняйте его к нулю.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# 2*x*2 + 4*x + 5 = 0
# или
# 2*x^2 + 4*x + 5 = 0

import random
def create_and_write_file(st):
    with open('file_for_tusk_33.txt', 'w') as data:
        data.write(st)

def rnd():
    return random.randint(0,101)

def create_rnd_list(k):
    my_list = [rnd() for i in range(k+1)]
    return my_list

def create_str(sp):
    my_list= sp[::-1]
    wr = ''
    if len(my_list) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(my_list)):
            if i != len(my_list) - 1 and my_list[i] != 0 and i != len(my_list) - 2:
                wr += f'{my_list[i]}x^{len(my_list)-i-1}'
                if my_list[i+1] != 0:
                    wr += ' + '
            elif i == len(my_list) - 2 and my_list[i] != 0:
                wr += f'{my_list[i]}x'
                if my_list[i+1] != 0:
                    wr += ' + '
            elif i == len(my_list) - 1 and my_list[i] != 0:
                wr += f'{my_list[i]} = 0'
            elif i == len(my_list) - 1 and my_list[i] == 0:
                wr += ' = 0'
    return wr

k = int(input("Введите натуральную степень k = "))
ratio = create_rnd_list(k)
create_and_write_file(create_str(ratio))
f = open('file_for_tusk_33.txt')
decision = f.read()
print(f'Ваш ответ: {decision}')
print('Вы также можете ознакомиться с ответом в файле "file_for_tusk_33.txt"')