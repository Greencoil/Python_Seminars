# 10(2) дополнительное задание. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 3D пространстве.
ax = float(input('Введите значения 1 точки на оси Х: '))
ay = float(input('Введите значения 1 точки на оси Y: '))
az = float(input('Введите значения 1 точки на оси Z: '))
bx = float(input('Введите значения 2 точки на оси Х: '))
by = float(input('Введите значения 2 точки на оси Y: '))
bz = float(input('Введите значения 2 точки на оси Z: '))


AB = (((ax - bx)**2 + (ay - by)**2 + (az - bz))**0.5)
AB = int(AB * 100) / 100

print(AB)