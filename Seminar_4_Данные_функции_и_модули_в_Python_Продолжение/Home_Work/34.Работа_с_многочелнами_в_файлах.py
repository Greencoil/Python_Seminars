# 34) Даны два файла, в каждом из которых находится запись многочлена, приравненного к нулю. Задача - сформировать файл, содержащий сумму многочленов (суммируем подобные слагаемые).
# Пример:
# 1 Файл : 2*x2 + 4*x + 5 = 0
# 2 Файл : 4*x2 + 7*x + 9 = 0
# 3 Файл: (содержит результат) 6*x2 + 11*x + 14 = 0
# Пример:
# 1 Файл : 2*x3 + 4*x2 + 5*x + 1 = 0
# 2 Файл : 4*x2 + 7*x + 9 = 0
# 3 Файл: (содержит результат) 2*x3 + 8*x2 + 12

first_file = open('1.first_file_tusk_34.txt', 'r')
second_file = open('2.second_file_tusk_34.txt', 'r')
final_file = open('3.final_file_tusk_34.txt', 'w')
file1 = first_file.readline()
file2 = second_file.readline()
for i in range(len(file1)):
    if file1[i-1] != '^':
        if file1[i].isnumeric():
            final_file.write(str(int(file1[i])+int(file2[i])))
        else:
            final_file.write(str(file1[i]))
    else:
        final_file.write(str(file1[i]))
first_file.close
second_file.close
final_file.close