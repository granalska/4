def input_error(func):
    """Декоратор для обробки типових помилок користувача."""
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter correct user name:"
        except ValueError:
            return "Give me name and phone please:"
        except IndexError:
            return "Enter user name:"
    return inner


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added"


@input_error
def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Contact updated"


@input_error
def show_phone(args, contacts):
    name = args[0]
    return f"{name}: {contacts[name]}"


@input_error
def show_all(contacts):
    if not contacts:
        return "Not found. Try again"
    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()


def main():
    contacts = {}
    print("Welcome to your bot")
    print("Commands: hello, add, change, phone, all ,exit, close")

    while True:
        user_input = input("Enter command:").strip()
        if not user_input:
            print("Enter argument for the command:")
            continue

        parts = user_input.split()
        command = parts[0].lower()
        args = parts[1:]

        if command == "hello":
            print("Can i help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command in ("exit", "close"):
            print("Completion of work...")
            break
        else:
            print("Unknown command. Try again")


if __name__ == "__main__":
    main()