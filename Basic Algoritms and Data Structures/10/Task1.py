water = 100
sugar = 50
lemon = 30
puree = 40

best_l = 0
best_s = 0

#пробуємо різну кількість лимонаду і соку
for l in range(51):
    for s in range(51):
        #рахуємо скільки треба води і пюре
        need_w = (l * 2) + s
        need_p = s * 2
        
        #перевірка чи вистачає всіх ресурсів
        if need_w <= water and l <= sugar and l <= lemon and need_p <= puree:
            
            #якщо сума напоїв більша за рекорд
            if l + s > best_l + best_s:
                best_l = l
                best_s = s

print(f"Лимонад: {best_l}")
print(f"Сік: {best_s}")