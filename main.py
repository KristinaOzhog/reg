from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

    # print(contacts_list)


pattern_tel = r'(\+7|8)?\s*\(?(\d+)\)?[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})((\s*)\(?(доб\.)\s*(\d+)\)?)?'
sub_tel = r'+7(\2)\3-\4-\5 \7\8\9'
pattern_name = r'(\w+)[\s](\w+)[\s](\w*)[\s]*'
sub_name = r'\1 \2 \3'
new_list = []
for cont in contacts_list:
    con = ' '.join(cont[:3])
    correct_names = re.sub(pattern_name, sub_name, con).split(' ')
    correct_phones = re.sub(pattern_tel, sub_tel, cont[5])
    cont_list = correct_names + [cont[3]] + [cont[4]] + [correct_phones] + [cont[6]]
    new_list.append(cont_list)
    # print(correct_names)

for c in new_list:
    for nc in new_list:
        if c[0] == nc[0] and c[1] == nc[1] and c is not nc:
            if c[2] == '':
                c[2] = nc[2]
            if c[3] == '':
                c[3] = nc[3]
            if c[4] == '':
                c[4] = nc[4]
            if c[5] == '':
                c[5] = nc[5]
            if c[6] == '':
                c[6] = nc[6]

# print(new_list)

result_lst = list()
for d in new_list:
    if d not in result_lst:
        result_lst.append(d)

print(result_lst)


with open("phonebook.csv", "w", encoding='utf-8', newline='') as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(result_lst)
