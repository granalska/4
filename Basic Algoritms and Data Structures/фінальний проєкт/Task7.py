import random

def monte_carlo_dice(num_trials=100000):
    sums = {i:0 for i in range(2,13)}

    for _ in range(num_trials):
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        s = d1 + d2
        sums[s] += 1

    #ймовірність 
    probabilities = {k: v/num_trials for k,v in sums.items()}
    return probabilities

#результат кидків
results = monte_carlo_dice()
for s in range(2,13):
    print(f"Сума {s}: ймовірність ≈ {results[s]*100:.2f}%")