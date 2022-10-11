# 7. Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print('x y z F')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             f = x or y or z
#             print(x, y, z, bool(f))

for x in range(2):
        for y in range(2):
            for z in range(2):
                F = (not (x or y or z)) == (not x and not y and not z)
                print(x, y, z, bool(F))

