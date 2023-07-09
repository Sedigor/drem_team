import pickle
from datetime import datetime
from pathlib import Path
import re
#from fake_content_2 import users


AB = [] #empty AddressBook


def write_AB(path, adr_book):
    with open(path, 'wb') as file:
            pickle.dump(adr_book, file)

def read_AB(path): 
    if path.exists():
        with open(path, 'rb') as file:
            return pickle.load(file)


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
        return f'\n| {self.name}| {self.phones}| {self.data_str}| {self.email}| {self.address}| # {self.notes}' 
        # return f'\n| {self.name:<25}| {self.phones:^20}| {self.data_str:^12}| {self.email:<33}| {self.address:<30}| # {self.notes:<20}' 
        # return'\n| {:<25}| {:^20}| {:^12}| {:<33}| {:<30}| # {:<20}'.format(self.name, 
        #                                                                      self.phones, 
        #                                                                      self.data_str, 
        #                                                                      self.email, 
        #                                                                      self.address, 
        #                                                                      self.notes)


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
            


def main():
    path_file = Path(__file__).parent / 'AddressBook.bin'
 
    for user in users:
        add_record(Record(**user))
        # print(user)

    # write_AB(path_file, AB)
    # AB = read_AB(path_file)
    print(AB)

 

if __name__ == "__main__":
    main()
