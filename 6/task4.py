def add_contact(args, contacts):
    if len(args) < 2:
        return "Використання: add Ім'я Номер"
    name, phone = args
    contacts[name] = phone
    return f"Контакт {name} додано."


def change_contact(args, contacts):
    if len(args) < 2:
        return "Використання: change Ім'я Новий_номер"
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return f"Номер для {name} змінено."
    else:
        return "Контакт не знайдено у базі."


def show_all_contacts(contacts):
    if contacts:
        result = []
        for name, phone in contacts.items():
            result.append(f"{name}: {phone}")
        return "\n".join(result)
    else:
        return "Список контактів порожній."


def show_phone(args, contacts):
    if len(args) < 1:
        return "Використання: phone Ім'я"
    name = args[0]
    if name in contacts:
        return f"{name}: {contacts[name]}"
    else:
        return "Контакт не знайдено."


def parse_input(user_input):
    parts = user_input.strip().split()
    cmd = parts[0].lower() if parts else ""
    args = parts[1:]
    return cmd, args


def main():
    contacts = {}
    print("Привіт! Я твій бот-помічник🤖")
    print("Команди: add, change, phone, all, exit")

    while True:
        user_input = input(">>> ")
        command, args = parse_input(user_input)

        if command in ("exit", "close"):
            print("Був радий допомогти. Бувай👋🏻")
            break

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all_contacts(contacts))

        else:
            print("Невідома команда. Перевірте правильність написання.")


if name == "main":
    main()