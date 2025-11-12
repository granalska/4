from collections import UserDict

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please"
        except KeyError:
            return "Enter correct user name"
        except IndexError:
            return "Enter user name"
    return inner


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if not (value.isdigit() and len(value) == 10):
            raise ValueError("Phone must contain 10 digits")
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
        raise ValueError("Old phone not found")

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
    message = "Contact updated"
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added"
    record.add_phone(phone)
    return message


@input_error
def change_contact(args, book):
    name, old, new = args
    record = book.find(name)
    if not record:
        raise KeyError
    record.change_phone(old, new)
    return "Phone changed"


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
        return "No contacts found"
    return "\n".join(str(r) for r in book.data.values())


def parse_input(text):
    parts = text.strip().split()
    return parts[0].lower(), parts[1:]


def main():
    book = AddressBook()
    print("Hi! I'm your assistant bot!")
    print("Commands: add, change, phone, all, exit")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["exit", "close"]:
            print("Good bye!")
            break
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(show_phone(args, book))
        elif command == "all":
            print(show_all(book))
        else:
            print("Invalid command")


if __name__ == "__main__":
    main()