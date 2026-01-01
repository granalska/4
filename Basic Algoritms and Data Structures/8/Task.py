import heapq

def connect_cabl(cables): 
    heapq.heapify(cables) #створ купи
    cost = 0

    while len(cables) > 1:
        s = heapq.heappop(cables) + heapq.heappop(cables) #зʼєднання самих коротких
        cost += s
        heapq.heappush(cables, s) #новий каб 

    return  cost #повертаємо

cables = [13, 2, 15, 7]

print(connect_cabl(cables)) #виводимо результ