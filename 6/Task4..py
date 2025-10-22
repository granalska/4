def add_contact(args,contacts):
    if len(args) < 2:
        return("Використання: add Ім'я yомер")
     
        name, phone = args
        contacts[name] = phone
        return f"Контакт {name} додано."    
    
    def change_contact(args,contacts):
        if len(args) < 2:
            return("Використання: change Ім'я новий_номер")
        name, new_phone = args
        if name in contacts:
            contacts[name] = new_phone
            return f"Номер для {name} змінено."
        else:
            return "контакт не здайдено у базі."
        
    def show_all_contacts(contacts):
            if contacts:
                result = []
                for name, phone in contacts.items():
                    result.append(f"{name}: {phone}")
                return "\n".join(result)
            else:
                return "Список контактів порожній."
            
def main():     

    contacts = {}  #контакти

    print("Привіт! Я твій бот-помічник🤖")
    print("Команди: add, change, phone, all, exit")

while True:
    user_input = input(">>> ").strip().split()

    if not user_input:
        continue  #пропуск якщо нічого не ввели 

    command = user_input[0].lower()  
    args = user_input[1:]            #аргументи 

    if command in ("exit", "close"):
        print("Був радий допомогти. Бувай👋🏻 ")
        break

    elif command == "add":
        if len(args) < 2:
            print("Використання: add Ім'я Номер")
        else:
            name = args[0]
            phone = args[1]
            contacts[name] = phone
            print(f"Контакт {name} додано.")

    elif command == "change":
        if len(args) < 2:
            print("Використання: change Ім'я Новий_номер")
        else:
            name = args[0]
            if name in contacts:
                contacts[name] = args[1]
                print(f"Номер для {name} змінено.")
            else:
                print("Такого контакту немає.")

    elif command == "phone":
        if len(args) < 1:
            print("Використання: phone Ім'я")
        else:
            name = args[0]
            if name in contacts:
                print(f"{name}: {contacts[name]}")
            else:
                print("Контакт не знайдено.")

    elif command == "all":
        if contacts:
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
        else:
            print("Список контактів порожній.")

    else:
        print("Невідома команда. Перевірте правильність написання.")

if __name__ == "__main__":
    main()  
    