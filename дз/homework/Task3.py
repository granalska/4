import re

#функ нормалізації 
def normalize_phone_numbers():
    #список номерів
    phone_numbers = [
        "+38(050)123-32-34",
        "0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11"
    ]

    unique_numbers = set()

    for phone in phone_numbers:
        #залишаємо лише цифри 
        cleaned = re.sub(r'\D', '', phone)

        #додаємо код країни
        if cleaned.startswith('0'):
            normalized = '+38' + cleaned
        elif cleaned.startswith('380'):
            normalized = '+' + cleaned
        else:
            
            continue

        # Перевірка довжиги номера
        if len(normalized) == 13:
            unique_numbers.add(normalized)

    return unique_numbers


#виведення
print("Нормалізовані номери телефонів:")
for number in normalize_phone_numbers():
    print(number)