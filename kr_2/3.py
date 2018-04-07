import re


def read_file():
    with open('xml_file.xml') as xml_file:
        file_str = xml_file.read()
        return file_str

def get_morph_res_dict(file_str):
    regexpr = r'<w>\n<ana lex="(?P<gr1>[а-я]+)" ' +\
        'gr="V=(?P<gr2>.*ед.*сов.*|.*сов.*ед.*)"/>\n(?P<gr3>[а-я]+)\n</w>'
    res_list = re.findall(regexpr, file_str)
    res_dict = dict()
    for res in res_list:
        if res not in res_dict:
            res_dict[res] = 0
        res_dict[res] += 1
    return res_dict

def write_to_file(res_dict):
    with open('result.csv', 'w', encoding='utf-8') as result_file: # безопасное открытие файла
        for it in res_dict:
            print(it)
            result_file.write(it[0] + ', ' + it[1] + ', ' +\
                              it[2] + ', ' + str(res_dict[it]) + '\n')

file_string = read_file()
res_dict = get_morph_res_dict(file_string)
res_list = res_dict.items()
write_to_file(res_dict)