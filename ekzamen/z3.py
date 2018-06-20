import os
import re


def get_file_str(news_item):
    with open('news' + os.sep + news_item, encoding='utf-8') as f:
        file_str = f.read()
    return file_str


def get_title(file_str):
    title = re.search(r'<title>(.+)</title>', file_str).group(1)
    return title


def get_word_list(file_str):
    return re.findall(r'<w>(.+)\n', file_str)
    # return re.findall(r'<w><ana lex="([A-ZА-ЯЁ]\w+)".+></ana>', file_str)


def find_NUM_gen(words_list, NUM_gen_dict):

    for w in words_list:

        if re.search(r'NUM', w) and re.search(r'gen'):

            if w not in NUM_gen_dict:
                NUM_gen_dict[w] = 0

            NUM_gen_dict[w] += 1



def write_file(words_dict):

    with open('task_2_result.txt', 'w', encoding='cp1251') as f:

        for key in words_dict:
            f.write(key + '\t' + str(upper_words_dict[key]) + '\n')


content_list = os.listdir('news/')

NUM_gen_dict = {}

for item in content_list:

    filestr = get_file_str(item)
    wordlist = get_word_list(filestr)

    print(wordlist)