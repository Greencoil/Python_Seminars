# 32) Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

user_list = list(map(int, input("Введите, пожалуйста, числа через пробел:\n").split()))
print(f"Исходный список: {user_list}")
source_list = []
[source_list.append(i) for i in user_list if i not in source_list]
print(f"Ваш список: {source_list}")
