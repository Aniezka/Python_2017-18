import os
import re


def get_file_str(news_item):
    with open('news' + os.sep + news_item, encoding='utf-8') as f:
        file_str = f.read()
    return file_str


def get_upper_word_list(file_str):
    return re.findall(r'<w><ana lex="([A-ZА-ЯЁ]\w+)".+></ana>', file_str)


def add_upper_word_to_dict(upper_dict, word_list):
    for w in word_list:

        if re.match(r'[XIV]+', w):
            continue

        if w not in upper_dict:
            upper_dict[w] = 0

        upper_dict[w] += 1

    return upper_dict


def write_table(upper_words_dict):

    with open('task_2_result.txt', 'w', encoding='utf-8') as f:

        for key in upper_words_dict:
            f.write(key + '\t' + str(upper_words_dict[key]) + '\n')


content_list = os.listdir('news/')
upper_words_dict = {}

for item in content_list:

    filestr = get_file_str(item)
    upperwordslist = get_upper_word_list(filestr)

    upper_words_dict = add_upper_word_to_dict(upper_words_dict, upperwordslist)

write_table(upper_words_dict)