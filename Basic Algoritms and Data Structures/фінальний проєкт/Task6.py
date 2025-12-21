#словник вартості та ккал
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 70

#жадібний алгоритм
items_sorted = sorted(items.items(), key=lambda x: x[1]["calories"]/x[1]["cost"], reverse=True)

total_cost = 0
total_calories = 0
chosen = []

for name, info in items_sorted:
    if total_cost + info["cost"] <= budget:
        chosen.append(name)
        total_cost += info["cost"]
        total_calories += info["calories"]

print("Жадібний вибір:", chosen)
print("Витрачені гроші:", total_cost)
print("Калорії:", total_calories)


#динамічний алгоритм
budget = 70
names = list(items.keys())
n = len(names)
costs = [items[name]["cost"] for name in names]
calories = [items[name]["calories"] for name in names]

#макс калорії при бюджеті
dp = [0]*(budget+1)
choice = [None]*(budget+1)

for i in range(n):
    for w in range(budget, costs[i]-1, -1):
        if dp[w-costs[i]] + calories[i] > dp[w]:
            dp[w] = dp[w-costs[i]] + calories[i]
            choice[w] = i

#відновлення вибору
w = budget
chosen = []
while w > 0 and choice[w] is not None:
    i = choice[w]
    chosen.append(names[i])
    w -= costs[i]

chosen.reverse()
print("Оптимальний вибір(DP):", chosen)
print("Макс калорії:", dp[budget])