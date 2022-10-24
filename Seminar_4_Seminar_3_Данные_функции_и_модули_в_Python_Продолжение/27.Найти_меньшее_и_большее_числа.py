# 27. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.

n = "1 2 3 45 5"
str_1 = n.split(' ')
new_list_1 = []
for i in str_1:
    new_list_1.append(int(i))
print(new_list_1)
print(max(new_list_1), min(new_list_1)) # с помощью функции
new_list_1.sort()
print(new_list_1[-1], new_list_1[0])
