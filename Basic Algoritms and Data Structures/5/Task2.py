def poshuk(spisok, shukane_chislo):
    left = 0
    right = len(spisok) - 1
    
    kroky = 0       #счетчик
    best_match = None #верхня межа або кращий вар

    while left <= right:
        kroky += 1  #робимо крок для кожної інерац
        
        mid = (left + right) // 2
        guess = spisok[mid] #серед число

        if guess >= shukane_chislo:
            #тут більше або рівно
            best_match = guess
            #переперевірка чи є щемваріант
            right = mid - 1
        else:
            left = mid + 1

    return (kroky, best_match)

#тестдрайв
numbers = [0.1, 1.3, 2.4, 3.6, 4.8]

result = poshuk(numbers, 2.0)

print(f"Кількість кроків:{result[0]}")
print(f"Верхня межа (найращий вибір):{result[1]}")
