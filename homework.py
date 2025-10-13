#завдання 1
from datetime import datetime, date
#функ підрахунку
def get_days_from_today(input_date):
    date_now = date.today()
    return (date_now - input_date).days
#вводимо дату та прописуємо помилку, далі виводимо результат
try:
     date_string = input("Введіть дату у форматі (дд.мм.рррр): ")
     date_input = datetime.strptime(date_string, "%d.%m.%Y").date()
     days_from_input = get_days_from_today(date_input)
    print(f"Days from {date_string}: {days_from_input}")

    date_string_my_b = "01.01.2001"
    date_my_b = datetime.strptime(date_string_my_b, "%d.%m.%Y").date()
    days_from_my_b = get_days_from_today(date_my_b)
    print(f"Days from my birthday: {days_from_my_b}")
except ValueError:
    print("Неправильний формат. Спробуйте ще раз.")

#завдання 2
#-----------------------------------------------------------

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

#завдання 3
#-----------------------------------------------------------

import re

#база даних
phone_numbers = [
     "    +38(050)123-32-34",
   "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   "]

#прибираємо зайве
    else "+38" + r if r.startswith("0")
    else "+" + r
    for r in (re.sub(r"[^\d]", "", p) for p in phone_numbers))
unique = dict.fromkeys(cleaned)

#виведення
for n in unique:
    if re.match(r"^\+380\d{9}$", n):
       print(n)

#завдання 4
#-----------------------------------------------------------
from datetime import datetime,timedelta

def get_upcoming_birthdays(users):
    
    today = datetime.today().date()
    upcoming_birthdays = []


    for user in users:
        #заміна рядка на дату
        birthday_str = user["birthday"]
        birthday_date = datetime.strptime(birthday_str, "%Y.%m.%d").date()

        #др цього року
        birthday_this_year = birthday_date.replace(year=today.year)

        #др наступного року
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year +1)

        #скільки днів до др
        days_left = (birthday_this_year - today).days

        #тижнева перевірка
        if days_left >= 0 and days_left <= 7:
            congratulation_date = birthday_this_year

            #перенос на пон, якщо на вихідні
            if congratulation_date.weekday() == 5:  # субота
                congratulation_date = congratulation_date+timedelta(days = 2)
            elif congratulation_date.weekday() == 6:  # неділя
                congratulation_date = congratulation_date+timedelta(days = 1)

            #додати до списку
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    
    return upcoming_birthdays
#дані робітників
users = [{"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}]

upcoming_birthdays = get_upcoming_birthdays(users)

print("Список привітань на цьому тижні:", upcoming_birthdays)