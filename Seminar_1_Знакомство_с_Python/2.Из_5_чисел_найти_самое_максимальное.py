# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
d = int(input('d = '))
e = int(input('e = '))

list = [a, b, c, d, e]
max = list[0]

# if list[1] > max:
#     max = list[1]
# if list[2] > max:
#     max = list[2] 
# if list[3] > max:
#     max = list[3]
# if list[4] > max:
#     max = list[4]

for i in list:
    if max < i:
        max = i

print(list)
print(f'Максимальное число: {max}')