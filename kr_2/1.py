import re


def read_file():
    with open('xml_file.xml') as xml_file:
        file_str = xml_file.read()  # считываем файл в строку
        return file_str  # и возвращаем ее


def get_n_symbols(file_str):
    regexpr = r'<body>\n(.*)\n</body>'
    line = re.findall(regexpr, file_str, flags=re.S)[
        0]  # находим совпадение - часть текста между строками <body> и </body>
    return len(line)  # возвращаем длину строки, в которую записана часть текста ...


def write_to_file(n_symbols):
    with open('result.txt', 'w', encoding='utf-8') as result_file:  # безопасное открытие файла
        result_file.write(str(n_symbols))


file_string = read_file()
n_symbols = get_n_symbols(file_string)
write_to_file(n_symbols)