import os
import re

content_list = os.listdir('.')

folder_list = []  # список, в который мы будем заносить названия подходящих папок

for item in content_list:  # проходимся по элементам списка с содержимым текущей директории
    if os.path.isdir(item):  # если элемент списка - директория, то:
        # если длины списков вхождений кириллических и латинских букв больше нуля
        if len(re.findall('[А-Яа-я]', item)) > 0 and len(re.findall('[A-Za-z]', item)) > 0:
            folder_list.append(item)  # добавляем элемент в список

print(len(folder_list), 'папок (папки) содержат в своем названии и кириллические, и латинские символы.')
print('Содержимое текущей директории:')

for item in content_list:
    if '.' in item:
        print('.'.join(re.split('\.', item)[:-1]))
    else:
        print(item)