from collections import UserDict
from datetime import datetime

class Field: 
    def __init__(self, value): 
        self.value = value

    def __str__(self): 
        return str(self.value)

class Name(Field): 
    pass

class Phone(Field):
    def __init__(self, value):
        if not (value.startswith("+380") and value[1:].isdigit() and len(value)==13):
            raise 
        ValueError("Телефон повинен бути у форматі: +380XXXXXXXXX")
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value):
        try: 
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
        except: 
            raise
        ValueError("Введіть дату у форматі: дд.мм.рррр")

class Record:
    def __init__(self, name):
        self.name, self.phones, self.birthday = Name(name), [], None

    def add_phone(self, p): 
        self.phones.append(Phone(p))

    def add_birthday(self, b): 
        self.birthday = Birthday(b)

    def __str__(self):
        ph = ", ".join(p.value for p in self.phones)
        bd = f", birthday: {self.birthday.value.strftime('%d.%m.%Y')}" 
        if self.birthday:
            pass
        else:
          return 
        f"{self.name.value}: {ph}{bd}"

class AddressBook(UserDict):
    def add_record(self, r): 
        self.data[r.name.value] = r

    def find(self, n): 
        return self.data.get(n)
    
    def delete(self, n): 
        self.data.pop(n, None)

    def get_upcoming_birthdays(self):

        today = datetime.today().date()
        res = []

        for r in self.data.values():
            if not r.birthday: continue
            b = r.birthday.value.replace(year=today.year)
            if b < today: b = b.replace(year=today.year+1)
            if (b - today).days <= 7: res.append((r.name.value, b.strftime("%d.%m.%Y")))
        return res


