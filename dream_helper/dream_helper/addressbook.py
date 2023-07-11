import pickle
from datetime import datetime
from pathlib import Path
import re
import os
from fake_content import users



# file_name = 'AddressBook.bin'
file_path = Path(__file__).parent / 'AddressBook.bin'
mp = '\nhelper>>_ '
separator = mp + "End option"

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
                    print(f'{mp}Error, incorrect date format')
            except ValueError as err:
                self.data_str = ''
                print(f'{mp}Error, ' + str(err))

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
       
    def info(self):
        print('\n| {:<15} {}\n|'.format('Contact info:', self.name))
        print('| {:<15}| {}'.format('Phones', ', '.join(self.phones)))
        print('| {:<15}| {}'.format('Birthday', self.data_str))
        print('| {:<15}| {}'.format('Email', self.email))
        print('| {:<15}| {}'.format('Address', self.address))
        print('| {:<15}| {}'.format('Notes', self.notes))
        # print('-' * 80)
        
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
        ab = pickle.load(fh)
    return ab
        
        
def init_addressbook():
    ab = []
    if os.path.exists(file_path):
        ab = read_ab(file_path)
    return ab


def days_to_birthday():
    ab = init_addressbook()
    today = datetime.today()
    found = {}
    for rec in ab:
        if rec.data_str:
            day, month, _ = map(int, rec.data_str.split('.'))
            next_birthday = datetime(today.year, month, day)
            if next_birthday < today:
                next_birthday = datetime(today.year + 1, month, day)
            days_left = (next_birthday - today).days
            found[rec.name] = [rec.data_str, days_left]
            # print(f"{mp}{rec.name}: days to next birthday {days_left}")
            # print(separator)
    print(mp,'Birthday info:\n')
    print('| {:<25}| {}'.format('Name', 'Birthday'))
    for k, v in found.items():
        print('| {:<25}| {}, {} days left'.format(k, v[0], v[1]))
    print(separator)
            
            
def edit_contact():
    ab = init_addressbook()
    print(mp,"Enter contact name to edit")
    name = input("\n>_ ")
    counter = 0
    
    for rec in ab:
        if rec.name == name:
            record = ab.pop(counter)
        counter +=1
    print(mp,'Choose edit option. add - Add phone number, del - Delete phone number')
    option = input("\n>_ ")
    print(mp, 'Enter phone number')
    phone = input("\n>_ ")
    
    if option == "add":
        record.add_new_phone(phone)
        ab.append(record)
        write_ab(file_path, ab)
        print(mp,"Contact has been updated")
        record.info()
        print(separator)
    
    if option == "del":
        record.del_phone(phone)
        ab.append(record)
        write_ab(file_path, ab)
        print(mp,"Contact has been updated")
        record.info()
        print(separator)

    
def del_record():
    ab = init_addressbook()
    print(mp,'Enter a contact name')
    name = input("\n>_ ")
    new_ab = list(filter(lambda record: record.name != name, ab))
    write_ab(file_path, new_ab)
    print(mp,'Address Book has been updated')
    print(separator)


# def find_in_record(part_str, flag_all=False, flag_name=True, flag_phone=True, flag_email=False, flag_address=False, flag_notes=False):
#     ab = init_addressbook()
#     out_str = []
    
#     if flag_all:
#         flag_name = True
#         flag_phone = True
#         flag_email = True
#         flag_address = True
#         flag_notes = True

#     for rec in ab:
#         if flag_name and part_str in rec.name:
#             out_str.append(f'\n {rec.name}')
            
#         if flag_phone:
#             phones = []
#             for phone in rec.phones:
#                 if part_str in phone:
#                     phones.append(phone)
#             if phones:
#                 out_str.append(f'\n {rec.name}: {phones}')

#         if flag_email and part_str in rec.email:
#             out_str.append(f'\n {rec.name}: {rec.email}')

#         if flag_address and part_str in rec.address:
#             out_str.append(f'\n {rec.name}: {rec.address}')

#         if flag_notes and part_str in rec.notes:
#             out_str.append(f'\n {rec.name}: {rec.notes}')

#     return out_str


def search_contact():
    ab = init_addressbook()
    found_contacts = []
    print(mp,'Write searching sample')
    sample = input("\n>_ ")

    for rec in ab:
        phones = ", ".join(rec.phones)
        if rec.name.find(sample) > -1 or phones.find(sample) > -1 or rec.email.find(sample) > -1:
            found_contacts.append(rec)
    print(mp,'Contacts found')
    for rec in found_contacts:
        rec.info()
    print(separator)
    

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
        print(mp,'Enter contact name')
        name = input("\n>_ ")
        if name in map(lambda record: record.name, ab):
            print(mp,'Contact already exists')
            continue
        break
        
    while True:
        print(mp,'Enter phone number. To skip press Enter')
        phone = input("\n>_ ")
        if not phone:
            phone = None
            break
        if is_valid_phone(phone):
            break
        print(mp,'Wrong number type')
        continue
        
    while True:
        print(mp,'Enter birthday in format dd-mm-yyyy. To skip press Enter')
        birthday = input("\n>_ ")
        if not birthday:
            birthday = None
            break
        if is_valid_birthday(birthday):
            break
        print(mp,'Wrong birthday type')
        continue

    while True:
        print(mp,'Enter email. To skip press Enter')
        email = input("\n>_ ")
        if not email:
            email = None
            break
        if is_valid_email(email):
            break
        print(mp,'Wrong email')
        continue
    
    print(mp,'Enter address. To skip press Enter')
    address = input("\n>_ ")
    if not address:
        address = None
    
    print(mp,'Add note to contact. To skip press Enter')    
    note = input("\n>_ ")
    if not note:
        note = ''
        
    record = Record(name, phone, birthday, email, address, note)
    ab.append(record)
    write_ab(file_path, ab)
    record.info()
    print(mp,'Contact added')
    print(separator)
    
    
def show_addressbook():
    ab = read_ab(file_path)
    if len(ab) == 0:
        print(separator)
        print(mp,"AddressBook is empty")
        print(separator)
    else:
        for record in ab:
            record.info()
    print(separator)


def find_show():
    while True:
        print(mp,'Choose option. all - shows all contacts in addressbook, find - searching contact by sample')
        command = input("\n>_ ")
        if command == "all":
            show_addressbook()
            break
        elif command == "find":
            search_contact()
            break
        else:
            print(mp,'Option is not exists')
            continue
    
    
def feed_addressbook():
    ab = init_addressbook()
    
    for user in users:
        record = Record(user['name'], user['phone'], user['birthday'], user['email'], user['address'], user['note'])
        ab.append(record)
    
    write_ab(file_path, ab)
        
        
# def main():
#     feed_addressbook()        
    # show_addressbook()
    # days_to_birthday()
    
    
    
# if __name__ == "__main__":
#     main()