def find_coins_greedy(keshbek, kassa):
    print(f"Видача решти з доступного номіналу: {keshbek}")

    nominal = {} #словник

    reversed = True 
    nominals = sorted(kassa.key(), reverse= True) #сортуємо від більш

    for groshy in nominals:
        while keshbek >= groshy and kassa[groshy] > 0:
            keshbek = keshbek - groshy #віддіємо кеш

            kassa[groshy] = kassa[groshy] - 1 #зменшуємо грн в касі


            if groshy in nominal: #запамʼятовуємо, що уже видали
                nominal[groshy] += 1
            else:
                nominal[groshy] = 1
            print(f"Видача: {groshy}, залишилось в терміналі: {kassa[groshy]}")

            if keshbek == 0:
                print(f"Ваша решта: {nominal}")

kassa= {50:2,
        10:1,
        2:1,
        1:1}
find_coins_greedy(113, kassa)