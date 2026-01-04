def find_min_coins(keshbek, kassa):
    print(f"Видача: {keshbek}")

    dp = [float('inf')] * (keshbek + 1)  #мін грошей треба для кожної суми 
    dp[0] = 0 
    
  #гроші які ми взяли останній раз 
    history = [0] * (keshbek + 1)
    
    nominals = kassa.keys() 

   
    for i in range(1, keshbek + 1):
        for groshy in nominals:
            #якщо кошти влазять і це швидше рішення 
            if i >= groshy and dp[i - groshy] + 1 < dp[i]:
                dp[i] = dp[i - groshy] + 1
                history[i] = groshy #запам'ятали хід з грошима

    nominal = {} #словник - результат
    
    if dp[keshbek] == float('inf'):
        print("Помилка видачі")
        return

    curr = keshbek
    while curr > 0:
        moneta = history[curr] 
        
        #додаємо в словник
        if moneta in nominal:
            nominal[moneta] += 1
        else:
            nominal[moneta] = 1
            
        curr = curr - moneta #мінус залишок

    print(f"Решта: {nominal}")
    print(f"Всього залишилось: {dp[keshbek]}")

kassa = {50:2, 10:1, 2:1, 1:1} 
find_min_coins(113, kassa)