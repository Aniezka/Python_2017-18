import re


def get_filename_and_length():
    filename = input("Введите имя файла: ")
    length = int(input("Введите количество букв: "))
    return filename, length


def fill_words_dict(filename):
    words_dict = {}
    inputFile = open(filename, "r", encoding="utf-8")
    for line in inputFile.readlines():
        line_results = get_un_words(line)
        for word in line_results:
            if word.lower() not in words_dict:
                words_dict[word] = 0
            words_dict[word.lower()] += 1
    inputFile.close()
    return words_dict
    
def get_un_words(text_str):
    reg_expr = "\s[Uu]n[a-z]+"
    raw_results = re.findall(reg_expr, text_str)
    results = []
    for res in raw_results:
        results.append(res[1:])
    return results

def print_perc(words_dict, l):
    results = words_dict.keys()
    print(len(results), "\"un-\" words at all")
    cnt = 0
    for res in results:
        if len(res) > l:
            cnt += 1
    print(str(cnt / len(results) * 100) + "% of them are longer than", l)

fname, l = get_filename_and_length()
words_dict = fill_words_dict(fname)
print_perc(words_dict, l)
