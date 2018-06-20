
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


def get_text(words_list):
    text = ''

    for w in words_list:
        match = re.search(r'<ana.+></ana>(.+)</w>(.+)?(</se>)?', w)

        text += match.group(1)
        if match.group(2) is not None:
            text += match.group(2)

        text = re.sub(r'`', '', text)
        text = re.sub(r'</se>', '', text)
        text += ' '

    return text


def write_file(item, newstext):
    filename = 'news_new' + os.sep + ''.join(item.split('.')[:-1]) + '.txt'

    with open(filename, 'w', encoding='cp1251') as f:
        f.write(newstext)


content_list = os.listdir('news/')
if not os.path.exists('news_new'):
    os.makedirs('news_new')

for item in content_list:

    filestr = get_file_str(item)
    wordslist = get_word_list(filestr)
    title = get_title(filestr)
    print(title)
    newstext = get_text(wordslist)
    write_file(item, title + '\n' + newstext)