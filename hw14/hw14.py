import re


def read_text_file(filename):
    # открываем текстовый файл в кодировке utf-8
    with open(filename, 'r', encoding='utf-8') as text_file:
        file_str = text_file.read()

    return file_str


def make_fragments(file_str):
    # делим текст на фрагменты
    fragments = re.split(r'[.!?…]\s|\?!\s|[\n\r]', file_str)

    return fragments


def filter_fragment(fragment):
    # убираем из фрагмента все, кроме слов - знаки препинания, кавычки, цифры
    # и символы, которые могли возникнуть, если текст был переведен в utf-8 из другой кодировки
    # (например, '\xa0')
    filtered_fragment = re.sub(r'[^a-zа-яё]+', ' ', fragment, flags=re.I).lower().strip()

    return filtered_fragment


def get_fragment_dict(fragment):
    # создаем словарь, в котором будут храниться пары "слово: количество его вхождений" для врагмента
    fragment_dict = {}

    for w in fragment.split():

        if w not in fragment_dict:
            fragment_dict[w] = 0

        fragment_dict[w] += 1

    return fragment_dict


def get_fragment_table(fragment):
    # создадим таблицу, в которой будут указаны слова предложения и количество вхождений
    # для слов, встречающихся более 1 раза
    f_fragment = filter_fragment(fragment)
    s_dict = get_fragment_dict(f_fragment)

    table_0 = 'Слова предложения: ' + f_fragment + '\n'  # исходная таблица
    res_table = table_0  # таблица - результат, в которую будем записывать строчки

    # пройдемся по всем словам предложения и впишем в таблицу те, которые
    # встречаются более одного раза
    # используется list comprehension и форматирование строк
    add_lines = ['{:^20}'.format(key) + '{:^5}'.format(str(s_dict[key])) + '\n' for key in s_dict if s_dict[key] > 1]
    res_table += ''.join(add_lines)

    if len(res_table) == len(table_0):
        res_table += 'В этом предложении все слова встречаются всего один раз\n'

    return res_table + '\n'


def get_result_line(fragments):
    # объединяем в линию строчки таблицы, полученной для каждого предложения
    # предложением считается фрагмент, содержащий буквы
    # используется list comprehension
    result_line = ''.join([get_fragment_table(s) for s in fragments if re.search('[a-zа-яё]+', s, flags=re.I)])

    return result_line


my_file_str = read_text_file(input('Введите имя файла: '))
my_fragments = make_fragments(my_file_str)
my_result_line = get_result_line(my_fragments)
print(my_result_line)