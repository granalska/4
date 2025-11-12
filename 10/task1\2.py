from collections import UserDict
from datetime import datetime, timedelta

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, KeyError, IndexError):
            return "Помилка. Не вірний формат"
    return inner


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if not (value.isdigit() and len(value) == 10):
            raise ValueError("Помилка. Телефон має складатись з 10 цифр")
        super().__init__(value)


class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Введіть в формваті DD.MM.YYYY")

    def __str__(self):
        return self.value.strftime("%d.%m.%Y")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def add_birthday(self, date):
        self.birthday = Birthday(date)

    def __str__(self):
        phones = ", ".join(p.value for p in self.phones)
        bd = f", birthday: {self.birthday}" if self.birthday else ""
        return f"{self.name.value}: {phones}{bd}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def get_upcoming_birthdays(self):
        today = datetime.today().date()
        next_week = today + timedelta(days=7)
        result = []
        for rec in self.data.values():
            if rec.birthday:
                bd = rec.birthday.value.replace(year=today.year)
                if today <= bd <= next_week:
                    result.append(f"{rec.name.value}: {bd.strftime('%d.%m.%Y')}")
        return result


@input_error
def add_birthday(args, book):
    name, date = args
    record = book.find(name)
    if not record:
        raise KeyError
    record.add_birthday(date)
    return f"До контакту {name} додана дата др."


@input_error
def show_birthday(args, book):
    name = args[0]
    record = book.find(name)
    if not record or not record.birthday:
        raise KeyError
    return f"В {name} др: {record.birthday}"


@input_error
def birthdays(args, book):
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "Наступного тижня немає запланованих др"
    return "\n".join(upcoming)


def parse_input(text):
    parts = text.strip().split()
    return parts[0].lower(), parts[1:]


def main():
    book = AddressBook()
    print("Привіт! Я твій бот-помічник;)")
    print("Команди: додати, додати др, показати др, усі др, вихід")

    while True:
        user_input = input("Ведіть команду:")
        command, args = parse_input(user_input)

        if command in ["Вихід"]:
            print("Завершення роботи:")
            break
        elif command == "Додати":
            name, phone = args
            record = book.find(name)
            if not record:
                record = Record(name)
                book.add_record(record)
            record.add_phone(phone)
            print("Контакт додано")
        elif command == "Додати др":
            print(add_birthday(args, book))
        elif command == "Подивитись др":
            print(show_birthday(args, book))
        elif command == "Дні народженяя":
            print(birthdays(args, book))
        elif command == "Усі др":
            print("\n".join(str(r) for r in book.data.values()) or "Відсутні контакти")
        else:
            print("Не відома команда")


if __name__ == "__main__":
    main()