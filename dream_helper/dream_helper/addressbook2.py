import pickle
from datetime import datetime
from pathlib import Path
import re
import os
#from fake_content_2 import users


# file_name = 'AddressBook.bin'
file_path = Path(__file__).parent / 'AddressBook.bin'
separator = "\n" + "-" * 50

class Record:
    def __init__(self, name, phone=None, birthday=None, email=None, address=None, notes=''): 
        self.name = name
        self.phones = []
        self.email = email
        self.address = address
        self.notes = notes
        
        if phone:            
            self.phones.append(phone)
        
        if birthday:   #format: 'dd.mm.YYYY or dd/mm/YYYY or dd-mm-YYYY'
            self.data_str = re.sub(r'[/-]', '.', birthday.strip())
            try:
                if self.data_str[-4:].isdigit():
                    self.birthday = datetime.strptime(self.data_str, '%d.%m.%Y')
                elif self.data_str[:4].isdigit(): #if format: 'YYYY.mm.dd or YYYY/mm/dd or YYYY-mm-dd'
                    self.birthday = datetime.strptime(self.data_str, '%Y.%m.%d')
                    self.data_str = self.birthday.strftime('%d.%m.%Y')
                else:
                    print('Error, incorrect date format')
            except ValueError as err:
                print('Error, ' + str(err))

        else:
            self.data_str = ''


    def __str__(self):
        # return f'\n| {self.name}| {self.phones}| {self.data_str}| {self.email}| {self.address}| # {self.notes}' 
        # return f'\n| {self.name:<25}| {self.phones:^20}| {self.data_str:^12}| {self.email:<33}| {self.address:<30}| # {self.notes:<20}' 
        return f'Name: {self.name}\nPhone number: {self.phones}\nBirthday: {self.data_str}\nEmail: {self.email}\nAddress: {self.address}\nNote: {self.notes}'


    def __repr__(self):
        return self.__str__()

    def add_new_phone(self, new_phone):
        self.phones.append(new_phone)
       

    def del_phone(self, phone=''):
        if not phone:
            self.phones.pop()  #delete the last phone number
        else:
            phone = phone.strip()
            if phone in self.phones:
                self.phones.remove(phone)
                return 'Phone number was deleted'
            else:
                return 'Error. This number is not in the phone list'


def write_ab(file_path, addressbook):
    with open(file_path, 'wb') as fh:
        pickle.dump(addressbook, fh)


def read_ab(file_path): 
    with open(file_path, 'rb') as fh:
        return pickle.load(fh)
        
        
def init_addressbook():
    ab = []
    if os.path.exists(file_path):
        ab = read_ab(file_path)
    return ab


AB = init_addressbook()


def add_record(record):
    AB.append(record)
    
    
def del_record(name):
    for i, rec in enumerate(AB):
        if rec.name == name:
            AB.pop(i)

def find_in_record(part_str, flag_all=False, flag_name=True, flag_phone=False, flag_email=False, flag_address=False, flag_notes=False):
    out_str = []
    if flag_all:
        flag_name = True
        flag_phone = True
        flag_email = True
        flag_address = True
        flag_notes = True

    for rec in AB:
        if flag_name and part_str in rec.name:
            out_str.append(f'\n {rec.name}')
            
        if flag_phone:
            phones = []
            for phone in rec.phones:
                if part_str in phone:
                    phones.append(phone)
            if phones:
                out_str.append(f'\n {rec.name}: {phones}')

        if flag_email and part_str in rec.email:
            out_str.append(f'\n {rec.name}: {rec.email}')

        if flag_address and part_str in rec.address:
            out_str.append(f'\n {rec.name}: {rec.address}')

        if flag_notes and part_str in rec.notes:
            out_str.append(f'\n {rec.name}: {rec.notes}')

    return out_str

            

def is_valid_birthday(birthday):
    try:
        day, month, year = map(int, birthday.split('-'))
        if day < 1 or day > 31 or month < 1 or month > 12 or len(str(year)) != 4:
            return False
    except ValueError:
        return False
    return True


def is_valid_phone(phone):
    phone = phone.strip()
    pattern = r'^\+?\d+[-.\s]?\(?\d{1,3}\)?[-.\s]?\d+[-.\s]?\d+$'
    
    if re.match(pattern, phone):
        return True
    else:
        return False
    

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False


def add_contact():
    ab = init_addressbook()
    while True:
        name = input("Enter contact name\n>_ ")
        for record in ab:
            if name == record.name:
                print('Contact already exists')
                continue
        break
        
    while True:
        phone = input("Enter phone number. To skip press Enter\n>_ ")
        if not phone:
            phone = None
            break
        if is_valid_phone(phone):
            break
        print('Wrong number type')
        continue
        
    while True:
        birthday = input("Enter birthday in format dd-mm-yyyy. To skip press Enter\n>_ ")
        if not birthday:
            birthday = None
            break
        if is_valid_birthday(birthday):
            break
        print('Wrong birthday type')
        continue

    while True:
        email = input("Enter email. To skip press Enter\n>_ ")
        if not email:
            email = None
            break
        if is_valid_email(email):
            break
        print('Wrong email')
        continue
    
    address = input("Enter address. To skip press Enter\n>_ ")
    if not address:
        address = None
        
    note = input("Add note to contact. To skip press Enter\n>_ ")
    if not note:
        note = ''
        
    record = Record(name, phone, birthday, email, address, note)
    ab.append(record)
    write_ab(file_path, ab)
    print('Contact added')
    print(separator)
    
    
def show_addressbook():
    ab = read_ab(file_path)
    for record in ab:
        print(record)
        print(separator)
    
    
def main():
    add_contact()
    show_addressbook()
    
    
    
if __name__ == "__main__":
    main()