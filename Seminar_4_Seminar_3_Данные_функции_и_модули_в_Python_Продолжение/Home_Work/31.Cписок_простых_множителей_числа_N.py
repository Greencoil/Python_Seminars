# 31) Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Пример: 70 = 2*5*7 => [2, 5, 7] # 140 = 2*2*5*7 => [2, 2, 5, 7]
                                  # 140|2
                                  # 70|2
                                  # 35|5
                                  # 7|7

n = int(input("Введите, пожалуйста, число: "))
i = 2
my_list = []
while i <= n:
    if n % i == 0:
        my_list.append(i)
        n //= i
        i = 2
    else:
        i += 1
print('Простые множители числа: ', my_list)