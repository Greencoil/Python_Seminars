# 13. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.
# Мое решение посимвольнео вхождение:
str_1 = input('Введите первую строку: ')
str_2 = input('Введите вторую строку: ')
count = 0

for i in str_1:
    for j in str_2:
        if i == j:
            count += 1

print(count)

# Рушение группы построчное вхождение:
# str1 = input('Введите первую строку: ')
# str2 = input('Введите вторую строку: ')
# count = 0
# k = 0
# if len(str2) > 1:
#     for i in range(1, len(str1)):
#         if str2 in str1[k:1]:
#             count += 1
#             k = i
# else:
#     for j in range(len(str1)):
#         if str1[j] == str2:
#             count += 1
# print(count)