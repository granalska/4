from collections import UserDict

class Field:

    def __init__(self, value): 
        self.value = value

    def __str__(self): 
        return self.value

class Name(Field): 
    pass

class Phone(Field):

    def __init__(self, value):
        if not (value.isdigit() and len(value) == 10):
            raise 
        ValueError("Телефон має містити 10 чисел")
        super().__init__(value)

class Record:

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone): 
        self.phones.append(Phone(phone))

    def remove_phone(self, phone): 
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old, new):
        for p in self.phones:
            if p.value == old: p.value = new

    def find_phone(self, phone):
        return next((p for p in self.phones if p.value == phone), None)
    
    def __str__(self):
        return f"{self.name.value}: {', '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):

    def add_record(self, rec):
        self.data[rec.name.value] = rec

    def find(self, name):
        return self.data.get(name)
    
    def delete(self, name): 
        self.data.pop(name, None)
