from datetime import datetime, date
#функ підрахунку
def get_days_from_today(input_date):
    date_now = date.today()
    return (date_now - input_date).days
#вводимо дату та прописуємо помилку, далі виводимо результат
try:
    date_string = "2020-10-09"
    #конвертація date
    date_input = datetime.strptime(date_string, "%Y-%m-%d").date()
    
    days_from_input = get_days_from_today(date_input)
    #вивід
    print(f"Кількість днів від {date_string}: {days_from_input}")

except ValueError:
    print("Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД'.")