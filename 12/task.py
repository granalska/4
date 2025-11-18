import pickle
from collections import UserDict
from datetime import datetime, timedelta

#декоратор помилок
def input_error(func): 
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter user name."
        except Exception as e:
            return f"Error: {e}"
    return inner


#класи:
class Field:
    def __init__(self, value):
        self.value = value

class Name(Field):      
    pass

class Phone(Field):
    def __init__(self, value):
        if not (value.isdigit() and len(value) == 10):
            raise ValueError("Phone must contain 10 digits") #валідація номеру
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY") #перевірка формату дати
    
    def __str__(self):
        return self.value.strftime("%d.%m.%Y")

class Record: #зберігання інформації про контакт
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def change_phone(self, old_phone, new_phone):
        for idx, p in enumerate(self.phones):
            if p.value == old_phone:
                self.phones[idx] = Phone(new_phone)
                return
        raise ValueError("Old phone not found")

    def add_birthday(self, date):
        self.birthday = Birthday(date)

    def __str__(self):
        phones = "; ".join(p.value for p in self.phones)
        birthday = f", birthday: {self.birthday}" if self.birthday else ""
        return f"Contact name: {self.name.value}, phones: {phones}{birthday}"

class AddressBook(UserDict): #зберігання та управління записами
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)
    
    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def get_upcoming_birthdays(self):
        today = datetime.today().date()
        upcoming_birthdays = []
        
        for record in self.data.values():
            if record.birthday:
                bday_this_year = record.birthday.value.replace(year=today.year)
                
                if bday_this_year < today:
                    bday_this_year = bday_this_year.replace(year=today.year + 1)
                
                days_delta = (bday_this_year - today).days

                if 0 <= days_delta <= 7:
                    congratulation_date = bday_this_year
                    if congratulation_date.weekday() == 5:
                        congratulation_date += timedelta(days=2)
                    elif congratulation_date.weekday() == 6:
                        congratulation_date += timedelta(days=1)

                    upcoming_birthdays.append(f"{record.name.value}: {congratulation_date.strftime('%d.%m.%Y')}")
        return upcoming_birthdays

#функ збереження та завантаження
    def save_data(book, filename="addressbook.pkl"):
      with open(filename, "wb") as f:
        pickle.dump(book, f)

    def load_data(filename="addressbook.pkl"):
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            return AddressBook()

#функ обробки команд
@input_error
def add_contact(args, book):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

@input_error
def change_contact(args, book):
    name, old_phone, new_phone, *_ = args
    record = book.find(name)
    if record:
        record.change_phone(old_phone, new_phone)
        return "Phone updated."
    else:
        raise KeyError

@input_error
def show_phone(args, book):
    name, *_ = args
    record = book.find(name)
    if record:
        return f"{name}: {', '.join(p.value for p in record.phones)}"
    else:
        raise KeyError

@input_error
def add_birthday(args, book):
    name, date, *_ = args
    record = book.find(name)
    if record:
        record.add_birthday(date)
        return "Birthday added."
    else:
        raise KeyError

@input_error
def show_birthday(args, book):
    name, *_ = args
    record = book.find(name)
    if record and record.birthday:
        return f"{name}'s birthday: {record.birthday}"
    else:
        return "Birthday not found or contact does not exist."

@input_error
def show_birthdays(args, book):
    birthdays = book.get_upcoming_birthdays()
    if not birthdays:
        return "No birthdays in the next week."
    return "\n".join(birthdays)

@input_error
def show_all(book):
    if not book.data:
        return "Address book is empty."
    return "\n".join(str(record) for record in book.data.values())

def parse_input(text):
    parts = text.strip().split()
    if not parts:
        return "", []
    return parts[0].lower(), parts[1:]

#головна логіка
def main():
    book = load_data()
    print("Welcome to the assistant bot!")
    print("Commands: add, change, phone, all, add-birthday, show-birthday, birthdays, exit")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            save_data(book)
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
        
        elif command == "add-birthday":
            print(add_birthday(args, book))
        
        elif command == "show-birthday":
            print(show_birthday(args, book))
        
        elif command == "birthdays":
            print(show_birthdays(args, book))
            
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
