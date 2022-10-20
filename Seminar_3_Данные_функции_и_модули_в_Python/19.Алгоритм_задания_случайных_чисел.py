# 19. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.
import time

def Random_Set(start = 0, end = 1):
    seconds = time.time()
    Next = True
    while Next:
        Rand = end * (seconds % 1)
        if Rand >= start or Rand >end: Next = False

    return int(Rand)

print(Random_Set(1, 100))