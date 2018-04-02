# Вариант 7

import re

def read_file():
    file_str = ''
    while file_str == '':
        filename = input('Введите имя файла:')
        try:
            with open(filename) as html_file:
                file_str = html_file.read() # считываем файл в строку
                return file_str # и возвращаем ее
        except:
            print('Ошибка') # если не удалось открыть файл, выводим сообщение об ошибке

def get_ISO_639_3_code(file_str):
    iso_regexpr = r'<th .*?>ISO 639-3</a></th>(.*?)</td>' # регулярное выражение для блока с кодом
    iso_line = re.findall(iso_regexpr, file_str, flags=re.S)[0] # находим совпадение
    code_regexpr = r'>(.*?)<' # регулярное выражение для кода
    code_list = re.findall(code_regexpr, iso_line)
    for el in code_list:
        if el != '':
            return el # когда нашли код, возвращаем его
      
def write_to_file(code):
    with open('result.txt', 'w', encoding='utf-8') as result_file: # безопасное открытие файла
        result_file.write(code)
        print('Code \'' + code + '\' is written to result.txt')

file_string = read_file()
code = get_ISO_639_3_code(file_string)
write_to_file(code)
