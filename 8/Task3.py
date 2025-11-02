def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except ValueError:
            return "Введіть імʼя та номер телефону"
        except KeyError:
            return "Відсутні збіги по номерам"
        except IndexError:
            return "Введіть імʼя"
    return inner

contacts = {}

@input_error
def add(args):
    name, phone = args
    contacts[name] = phone
    return "Створено новий контакт"

@input_error
def phone(args):
    return contacts[args[0]]

def all_contacts():
    return "\n".join(f"{n}: {p}" for n, p in contacts.items()) or "Немає контактів"

while True:
    cmd = input("Команди (Створити, Номери, Усі контакти, Вихід): ").lower()
    if cmd == "Вихід":
        print("Завершення роботи")
        break
    elif cmd == "Створити":
        print(add(input("Введіть імʼя та номер: ").split()))
    elif cmd == "Номер":
        print(phone(input("Введіть номер: ").split()))
    elif cmd == "Усі контакти":
        print(all_contacts())
    else:
        print("Помилка виконання")