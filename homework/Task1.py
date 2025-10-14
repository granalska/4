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