import random

#кількість кидків
shots = 100000
hits = 0

#кидаємо методом тика
for i in range(shots):
    #x від 0 до 2
    x = random.uniform(0, 2)
    #y від 0 до 4
    y = random.uniform(0, 4)

    #якщо точка потрапила під графік
    if y <= x**2:
        hits += 1

#площа всього прямокутника (2 * 4 = 8)
area_box = 8

#рахуємо сіру площу
final_area = (hits / shots) * area_box

print(f"Площа: {final_area}")