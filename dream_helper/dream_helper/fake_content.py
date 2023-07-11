from faker import Faker
import random


fake = Faker(['uk_UA'])

list_codes = ['050', '066', '095', '099', '067', '068', '096', '097', '063', '073', '093']

def generate_phone_number():
    # prefix = "+380"
    # body = ""
    # for _ in range(7):
    #     num = random.randint(0, 9)
    #     body += str(num)
    # phone_number = prefix + body

    phone_number = '+38' + str(random.choice(list_codes)) + str(random.randint(1000000, 9999999))
    
    return phone_number


TRANSLIT = {1072: 'a', 1040: 'A', 1073: 'b', 1041: 'B', 1074: 'v', 1042: 'V', 1075: 'g', 1043: 'G', 1076: 'd', 1044: 'D', 
        1077: 'e', 1045: 'E', 1105: 'jo', 1025: 'JO', 1078: 'zh', 1046: 'ZH', 1079: 'z', 1047: 'Z', 1080: 'i', 1048: 'I', 
        1081: 'j', 1049: 'J', 1082: 'k', 1050: 'K', 1083: 'l', 1051: 'L', 1084: 'm', 1052: 'M', 1085: 'n', 1053: 'N', 
        1086: 'o', 1054: 'O', 1087: 'p', 1055: 'P', 1088: 'r', 1056: 'R', 1089: 's', 1057: 'S', 1090: 't', 1058: 'T', 
        1091: 'u', 1059: 'U', 1092: 'f', 1060: 'F', 1093: 'h', 1061: 'H', 1094: 'ts', 1062: 'TS', 1095: 'ch', 1063: 'CH', 
        1096: 'sh', 1064: 'SH', 1097: 'sch', 1065: 'SCH', 1098: '', 1066: '', 1099: 'y', 1067: 'Y', 1100: "", 1068: "", 
        1101: 'e', 1069: 'E', 1102: 'yu', 1070: 'YU', 1103: 'ya', 1071: 'YA', 1108: 'ie', 1028: 'IE', 1110: 'i', 1030: 'I', 
        1111: 'ji', 1031: 'JI', 1169: 'g', 1168: 'G', 39: ''}

def create_fake_users(fake, n=20):
    users = []
    for _ in range(n):
        user = {}
        user["name"] = fake.name()
        user["phone"] = generate_phone_number()
        user["birthday"] = str(fake.date_of_birth(None, 21, 50)) # вік від 21 до 50 років     #date()
        user["email"] = user["name"].lower().replace(" ", "_").translate(TRANSLIT) + "@" + fake.free_email_domain()
        # user["email"] = user["name"].lower().replace(" ", "_") + "@" + fake.free_email_domain()
        user["address"] =  fake.address()#fake.street_address()
        user["note"] = fake.sentence(nb_words=6)
        users.append(user)
    return users


def random_user(users):
    user = random.choice(users)
    return user

users = create_fake_users(fake)
user_1 = random_user(users)
user_2 = random_user(users)

# print(users)

if __name__ == '__main__':
    for user in users:
        print("| {:<25}| {:^16}| {:^16}| {:<33}| {:<16}".format(user["name"], 
                                                            user["phone"], 
                                                            user["birthday"], 
                                                            user["email"], 
                                                            user["address"]
                                                            ))