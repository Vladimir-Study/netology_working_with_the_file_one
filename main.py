import os

BASE_DIR = os.getcwd()
LOGS_DIR = 'files'
LOG_FILE_NAME = 'recipes.txt'
FILE_ONE = '1.txt'
FILE_TWO = '2.txt'
FILE_THREE = '3.txt'
RESULT_FILE = 'result.txt'
file = os.path.join(BASE_DIR, LOGS_DIR, LOG_FILE_NAME)
file_one = os.path.join(BASE_DIR, LOGS_DIR, FILE_ONE)
file_two = os.path.join(BASE_DIR, LOGS_DIR, FILE_TWO)
file_three = os.path.join(BASE_DIR, LOGS_DIR, FILE_THREE)
write_file = os.path.join(BASE_DIR, LOGS_DIR, RESULT_FILE)

list_cook_book = [[]]
cook_book = {}

with open(file, encoding='utf-8') as f:
    for line in f:
        if line != '\n':
            list_cook_book[-1].append(line.strip())
        else:
            list_cook_book.append([])

for lst in list_cook_book:
    cook_book[lst[0]] = []
    for engredient in lst[2:]:
        engredient_list = engredient.split('|')
        cook_book[lst[0]].append(
            {'ingredient_name': engredient_list[0], 'quantity': engredient_list[1], 'measure': engredient_list[2]})


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for key in cook_book.keys():
            if dish == key:
                for i in cook_book[key]:
                    if i['ingredient_name'] not in shop_list:
                        shop_list[i['ingredient_name']] = {'measure': i['measure'],
                                                           'quantity': int(i['quantity']) * int(person_count)}
                    else:
                        sum_quantity = int(shop_list[i['ingredient_name']]['quantity']) * int(person_count)
                        shop_list[i['ingredient_name']] = {'measure': i['measure'], 'quantity': sum_quantity}
    return shop_list


show = get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2)
for key, val in show.items():
    print(f'{key}: {val}')

files_contents = []
with open(file_one, encoding='utf-8') as f_one:
    list_file_one = [FILE_ONE + '\n']
    content_file_one = f_one.readlines()
    list_file_one.append(str(len(content_file_one)) + '\n')
    for line in content_file_one:
        list_file_one.append(line)
    list_file_one.append('\n')
    files_contents.append(list_file_one)

with open(file_two, encoding='utf-8') as f_two:
    list_file_two = [FILE_TWO + '\n']
    content_file_two = f_two.readlines()
    list_file_two.append(str(len(content_file_two)) + '\n')
    for line in content_file_two:
        list_file_two.append(line)
    list_file_two.append('\n')
    files_contents.append(list_file_two)

with open(file_three, encoding='utf-8') as f_three:
    list_file_three = [FILE_THREE + '\n']
    content_file_three = f_three.readlines()
    list_file_three.append(str(len(content_file_three)) + '\n')
    for line in content_file_three:
        list_file_three.append(line)
    list_file_three.append('\n')
    files_contents.append(list_file_three)


with open(write_file, 'a', encoding='utf-8') as f_w:
    for file_content in sorted(files_contents, key=len):
        f_w.writelines(file_content)