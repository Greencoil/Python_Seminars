# 28. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1. с помощью математических формул нахождения корней квадратного уравнения


A = float(input('Введите A: '))
B = float(input('Введите B: '))
C = float(input('Введите C: '))
D = B ** 2 - 4 * A * C
if D == 0:
    x = -B/(2*A)
    print(f'Уровнение имеет корень {x}')
elif D > 0:
    x1 = (-B + D**0.5)/(2*A)
    x2 = (-B - D**0.5)/(2*A)
    print(f'Уровнение имеет корни: {x1} и {x2}')
else:
    print('Уровнение не имеет корней')


