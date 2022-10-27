# 30) Вычислить число π c заданной точностью d
# Пример: при d = 0.001,π = 3.141 10^(-1)≤d≤10^(-10)


from math import pi
i = int(input('Введите, пожалуйста, количество знаков после запятой в числе ПИ: '))
h = 0
b = list()
for x in str(pi):
    h += 1
    b.append(x)
    if h == i+2:
        break
h = ''.join(b)
print(h)