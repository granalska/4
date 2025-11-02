from collections import UserDict
from datetime import datetime, date

class Field: 
    def __init__(self, value): 
        self.value = value

class Name(Field): 
    pass

class Phone(Field):
    def __init__(self, value):
        if not (value.isdigit() and len(value)==10):
            raise 
        ValueError("Телефон має містити 10 цифр")
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
        except: 
            raise 
        ValueError("Формат має бути дд.мм.рррр")

class Record:
    def __init__(self, name):
        self.name, self.phones, self.birthday = Name(name), [], None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def add_birthday(self, b): 
        self.birthday = Birthday(b)

    def __str__(self):
        ph = ", ".join(p.value for p in self.phones) or "Відсутній номер"
        bd = f", birthday: {self.birthday.value.strftime('%d.%m.%Y')}" 
        if self.birthday:
            pass
        else:
          return f"{self.name.value}: {ph}{bd}"

class AddressBook(UserDict):
    def add_record(self, r): 
        self.data[r.name.value] = r

    def find(self, name): 
        return self.data.get(name)
    
    def get_upcoming_birthdays(self):
        today = date.today(); res = []
        for r in self.data.values():
            if not r.birthday: 
                continue
            bd = r.birthday.value.replace(year=today.year)
            if bd < today: bd = bd.replace(year=today.year + 1)
            if (bd - today).days <= 7:
                res.append(f"{r.name.value}: {bd.strftime('%d.%m.%Y')}")
        return res or ["Найближчим часом свята відсутні"]

def input_error(func):

    def wrapper(*a):
        try: 
            return func(*a)
        except Exception as e: 
            return str(e)
    return wrapper

@input_error

def add_contact(args, book):
    name, phone, *_ = args
    r = book.find(name)
    if not r: 
        r = Record(name); book.add_record(r)
    r.add_phone(phone)
    return "Контакт збережено"

@input_error

def add_birthday(args, book):
    name, b = args; book.find(name).add_birthday(b); 
    return "Створено нову подію"

@input_error

def show_birthday(args, book):
    return book.find(args[0]).birthday.value.strftime("%d.%m.%Y")

@input_error

def birthdays(args, book):
    return "\n".join(book.get_upcoming_birthdays())

def parse_input(t): 
    return t.strip().split()

def main():

    book = AddressBook()
    print("Привіт! Я твій бот-помічник")

    while True:
        c, *a = parse_input(input("Введення: "))

        if c in ["Вихід", "Завершити"]: print("Exit"); break

        elif c == "Створити": print(add_contact(a, book))

        elif c == "Додати ДР": print(add_birthday(a, book))

        elif c == "Переглянути контакти": print(show_birthday(a, book))

        elif c == "День народження": print(birthdays(a, book))

        elif c == "Усі контакти":

            for r in book.values(): print(r)
        else: print("Невідома команда")

if __name__ == "__main__": main()