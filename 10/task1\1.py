from collections import UserDict

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "введіть імʼя та телефон"
        except KeyError:
            return "введіть коректне "
        except IndexError:
            return "введіть імʼя користувача"
    return inner


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if not (value.isdigit() and len(value) == 10):
            raise ValueError("")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def change_phone(self, old, new):
        for ph in self.phones:
            if ph.value == old:
                ph.value = new
                return
        raise ValueError("старий иконтакт не знайдено")

    def __str__(self):
        phones = ", ".join(p.value for p in self.phones)
        return f"{self.name.value}: {phones}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)


@input_error
def add_contact(args, book):
    name, phone, *_ = args
    record = book.find(name)
    message = "контакт оновлено"
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "контакт збережено"
    record.add_phone(phone)
    return message


@input_error
def change_contact(args, book):
    name, old, new = args
    record = book.find(name)
    if not record:
        raise KeyError
    record.change_phone(old, new)
    return "телефон змінено"


@input_error
def show_phone(args, book):
    name = args[0]
    record = book.find(name)
    if not record:
        raise KeyError
    return f"{name}: {', '.join(p.value for p in record.phones)}"


@input_error
def show_all(book):
    if not book.data:
        return "немає збігів"
    return "\n".join(str(r) for r in book.data.values())


def parse_input(text):
    parts = text.strip().split()
    return parts[0].lower(), parts[1:]


def main():
    book = AddressBook()
    print("Привіт! Ятвій бот-помічник;)")
    print("команди: додати, змінити, телефон, усі, вихід")

    while True:
        user_input = input("введіть командук")
        command, args = parse_input(user_input)

        if command in ["вихіж"]:
            print("завершення роботи...")
            break
        elif command == "додати":
            print(add_contact(args, book))
        elif command == "змінити":
            print(change_contact(args, book))
        elif command == "телефон":
            print(show_phone(args, book))
        elif command == "усі":
            print(show_all(book))
        else:
            print("не відома команда")


if __name__ == "__main__":
    main()