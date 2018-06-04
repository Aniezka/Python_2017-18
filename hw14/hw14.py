import re


def read_text_file(filename):

    with open(filename, 'r', encoding='utf-8') as text_file:
        file_str = text_file.read()

    return file_str


def make_sentences(file_str):

    file_str_corr = file_str.replace(u'\xa0', u' ')  # убираем возможные \xao, обозначающие пробелы в кодировке Unicode
    sentences = re.split(r'[.!?…]\s|\?!\s|[\n\r]', file_str_corr)  # делим текст на предложения

    return sentences


def filter_sentence(sentence):

    filtered_sentence = re.sub(r'[^А-Яа-я]+', ' ', sentence).lower().strip()  # убираем из предложения все, кроме слов

    return filtered_sentence


def get_one_sentence_dict(sentence):

    sentence_dict = {}  # в этом словаре будут храниться пары "слово: количество его вхождений"

    for w in sentence.split():

        if w not in sentence_dict:
            sentence_dict[w] = 0

        sentence_dict[w] += 1

    return sentence_dict


def get_sentence_table(sentence):

    f_sentence = filter_sentence(sentence)
    s_dict = get_one_sentence_dict(f_sentence)

    table_0 = 'Слова предложения: ' + f_sentence + '\n'  # исходная таблица
    res_table = table_0  # таблица - результат, в которую будем записывать строчки

    # с помощью list comprehension пройдемся по всем словам предложения и впишем в таблицу те, которые
    # встречаются более одного раза
    add_lines = ['{:^20}'.format(key) + '{:^5}'.format(str(s_dict[key])) + '\n' for key in s_dict if s_dict[key] > 1]
    res_table += ''.join(add_lines)

    if len(res_table) == len(table_0):
        res_table += 'В этом предложении все слова встречаются всего один раз\n'

    return res_table + '\n'


def get_result_line(sentences):

    result_line = ''.join([get_sentence_table(s) for s in sentences if re.match('.*[а-я]+', s, re.I)])

    return result_line


# my_file_str = read_text_file('Belaya_gvardia_cut_utf-8.txt')
my_file_str = read_text_file('test.txt')
my_sentences = make_sentences(my_file_str)
my_result_line = get_result_line(my_sentences)
print(my_result_line)
