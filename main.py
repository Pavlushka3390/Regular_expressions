import re
import csv
from pprint import pprint

with open("phonebook_raw.csv", encoding='UTF-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)



def phone_number(contacts_list):
  number_pattern_raw = r'(\+7|8)(\s*)(\(*)(\d{3})(\)*)(\s*)' \
                       r'(\-*)(\d{3})(\s*)(\-*)(\d{2})(\s*)(\-*)' \
                       r'(\d{2})(\s*)(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*)'
  number_pattern_new = r'+7(\4)\8-\11-\14\15\17\18\19\20'
  contacts_list_updated = list()
  for card in contacts_list:
    card_as_string = ','.join(card)
    formatted_card = re.sub(number_pattern_raw, number_pattern_new, card_as_string)
    card_as_list = formatted_card.split(',')
    contacts_list_updated.append(card_as_list)
  return contacts_list_updated

def contacts_name(contacts_list):
  name_pattern_raw = r'^([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]+)' \
                       r'(\s*)(\,?)([А-ЯЁа-яё]*)(\,?)(\,?)(\,?)'
  name_pattern_new = r'\1\3\10\4\6\9\7\8'
  contacts_list_updated = list()
  for card in contacts_list:
    card_as_string = ','.join(card)
    formatted_card = re.sub(name_pattern_raw, name_pattern_new, card_as_string)
    card_as_list = formatted_card.split(',')
    contacts_list_updated.append(card_as_list)
  return contacts_list_updated

def duplicates(contacts_list):
  for i in contacts_list:
    for j in contacts_list:
      if i[0] == j[0] and i[1] == j[1] and i is not j:
        if i[2] == '':
          i[2] = j[2]
        if i[3] == '':
          i[3] = j[3]
        if i[4] == '':
          i[4] = j[4]
        if i[5] == '':
          i[5] = j[5]
        if i[6] == '':
          i[6] = j[6]
  contacts_list_updated = list()
  for card in contacts_list:
    if card not in contacts_list_updated:
      contacts_list_updated.append(card)
  return contacts_list_updated

def write_file(contacts_list):
  with open("phonebook.csv", "w") as f:
    data_writer = csv.writer(f, delimiter=',')
    data_writer.writerows(contacts_list)

if __name__ == '__main__':
  contacts = phone_number(contacts_list)
  contacts = contacts_name(contacts)
  contacts = duplicates(contacts)
  with open("phonebook.csv", "w", encoding='UTF-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts)
  print(contacts)