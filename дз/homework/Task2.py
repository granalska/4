import random
# функція підрахунку
def get_numbers_ticket(quantity, min_num, max_num):
    if not (1 <= min_num < max_num <= 1000):
        print("Неправильний діапазон чисел (має бути від 1 до 1000)")
        return []

    try:
        return sorted(random.sample(range(min_num, max_num + 1), quantity))
    except ValueError:
        print(f"Неможливо вибрати {quantity} унікальних чисел з діапазону {min_num}-{max_num}")
        return []

print("Ваші лотерейні числа:", get_numbers_ticket(6, 1, 49))
print("Ваші лотерейні числа:", get_numbers_ticket(5, 1, 36))