import queue

# Створити чергу заявок
reguest_queue = queue.Queue()

reguest_id = 1

# Функція 
def generate_request():
    # Створити нову заявку
    # Додати заявку до черги
    global reguest_id
    request = f"Request_{request_id}"
    request_id += 1
    request_queue.put(request)
    print(f"Створено: {request}")

def process_request():
#     Якщо черга не пуста:
#         Видалити заявку з черги
#         Обробити заявку
    if not request_queue.empty():
        request = request_queue.get()
        print(f"Заявка оброблена: {request}")
#     Інакше:
#         Вивести повідомлення, що черга пуста
    else:
        print("Черга пуста")
    

# Головний цикл програми:
while True:
    print("\n Add - створити заявку")
    print("Process - обробити заявку")
    print("Exit - вихід")
#     Поки користувач не вийде з програми:
#         Виконати generate_request() для створення нових заявок
#         Виконати process_request() для обробки заявок
    choice = input("Виберіть команду:").lower()

    if choice == "Add":
        generate_request()
    elif choice == "Process":
        process_request()
    elif choice == "Exit":
        print("Вихід із програми")
        break
    else:
        print("Невідома команда")
