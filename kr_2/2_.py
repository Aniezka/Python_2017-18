import re


def read_file():
    with open('xml_file.xml') as xml_file:
        file_str = xml_file.read()
        return file_str


def get_morph_res_dict(file_str):
    regexpr = r'<w>\n<ana lex="[а-я]+" gr="(.*)"/>\n[а-я]+\n</w>'
    res_list = re.findall(regexpr, file_str)
    res_dict = dict()
    for res in res_list:
        if res not in res_dict:
            res_dict[res] = 0
        res_dict[res] += 1
    return res_dict


def get_sorted_res(res_dict):
    sorted_res = sorted(res_dict.items(), key=lambda entry: entry[1], reverse=True)
    return sorted_res


def write_to_file(sorted_res_list):
    with open('result.txt', 'w', encoding='utf-8') as result_file:  # безопасное открытие файла
        for el in sorted_res_list:
            result_file.write(el[0] + '\n')


file_string = read_file()
res_dict = get_morph_res_dict(file_string)
sorted_res_list = get_sorted_res(res_dict)
write_to_file(sorted_res_list)