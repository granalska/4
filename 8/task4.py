def input_error(func):
    """Декоратор для обробки типових помилок користувача."""
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Введіть своє імʼя:"
        except ValueError:
            return "Ведіть номер телефону:"
        except IndexError:
            return "Введіть імʼя користувача:"
    return inner


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Контакт додано"


@input_error
def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Контакт оновлено"


@input_error
def show_phone(args, contacts):
    name = args[0]
    return f"{name}: {contacts[name]}"


@input_error
def show_all(contacts):
    if not contacts:
        return "Немає збігівю Повторіть спробу"
    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()


def main():
    contacts = {}
    print("Привіт! Я твій бот-помічник;)")
    print("Команди: додати контакт, змінити контакт, номер, усі контакти, вихід")

    while True:
        user_input = input("Введіть команду:").strip()
        if not user_input:
            print("Агргумент для команди:")
            continue

        parts = user_input.split()
        command = parts[0].lower()
        args = parts[1:]

        if command == "Додати контакт":
            print(add_contact(args, contacts))
        elif command == "Змінити контакт":
            print(change_contact(args, contacts))
        elif command == "Номер":
            print(show_phone(args, contacts))
        elif command == "Усі контакти":
            print(show_all(contacts))
        elif command == "Вихід":
            print("Завершення роботи,..")
            break
        else:
            print("Невідома команда. Повторіть знову")


if __name__ == "__main__":
    main()