import pickle

class Record:
    def __init__(self, name, phone=None, email=None):
        self.name = name
        self.phone = phone
        self.email = email

    def __repr__(self):
        return f"{self.name}, {self.phone}, {self.email}"


class AddressBook:
    def __init__(self):
        self.records = {}

    def add_record(self, record):
        self.records[record.name] = record

    def find(self, name):
        return self.records.get(name)

    def remove(self, name):
        if name in self.records:
            del self.records[name]

    def __repr__(self):
        return "\n".join(str(rec) for rec in self.records.values())

def save_data(book, filename="addressbook.pkl"):
    """Зберігає об’єкт AddressBook у файл"""
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename="addressbook.pkl"):
    """Завантажує AddressBook із файлу або створює новий, якщо файлу немає"""
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        print("Файл не знайдено. Створення нової адресної книги")
        return AddressBook()
    except Exception as e:
        print(f"Помилка при завантаженні даних:{e}")
        return AddressBook()

def main():
    book = load_data()

    while True:
        command = input("\nКоманда(add/find/show/exit):").strip().lower()

        if command == "add":
            name = input("Ім'я: ")
            phone = input("Телефон: ")
            email = input("Email: ")
            record = Record(name, phone, email)
            book.add_record(record)
            print("Запис додано")

        elif command == "find":
            name = input("Введіть ім'я:")
            record = book.find(name)
            print(record if record else "Не знайдено")

        elif command == "show":
            print("\nАдресна книга:")
            print(book if book.records else "Порожня")

        elif command == "exit":
            save_data(book)
            print("Дані збережено. Вихід…")
            break

        else:
            print("Невідома команда. Спробуйте ще раз")


if __name__ == "__main__":
    main()