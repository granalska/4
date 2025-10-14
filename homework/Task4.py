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