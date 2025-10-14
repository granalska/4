import random
#функ підрахунку
def get_numbers_ticket(quantity, min=1, max=1000):
    if quantity > (max - min + 1):
        raise ValueError("Не відповідає кількості в діапазоні")
    ticket_numbers = random.sample(range(min, max + 1), quantity)
    ticket_numbers.sort()
    return ticket_numbers

print("Ваші лотерейні числа:", get_numbers_ticket(6, 1, 49))
print("Ваші лотерейні числа:", get_numbers_ticket(5, 1, 36))