from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value: str):
        value = str(value).strip()
        if not value:
            raise ValueError("Пустий рядок не приймається")
        super().__init__(value)

class Phone(Field):
    def __init__(self, value: str):
        value = str(value)
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number doesn't contain 10 digits")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # реалізація класу
    def add_phone(self, phone:str):
        self.phones.append(Phone(phone))

    def edit_phone(self, old_phone: str, new_phone: str):
        p = self.find_phone(old_phone)
        if p is None:
            raise ValueError(f"Old phone {old_phone} not found")
        p.value = Phone(new_phone).value

    def find_phone(self, phone:str):
        for p in self.phones:
            if p.value == phone:
                return p
        return None
    
    def remove_phone(self, phone: str) -> bool:
        p = self.find_phone(phone)
        if p is None:
            raise ValueError("Nothing to remove")
        self.phones.remove(p)
        return True

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
   

class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())

    def delete(self, name:str):
          return self.data.pop(name)
    
    def find(self, name:str):
          if name in self.data:
                return self.data[name]
          else:
                return None
          
# Створення нової адресної книги
book = AddressBook()

 # Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
john_record.add_phone("4445555222")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
print(book)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("5555555555", "1112223334")

print(john)

found_phone = john.find_phone("4445555222")
print(f"{john.name}: {found_phone}")
book.delete("Jane")
