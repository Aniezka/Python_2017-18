import re


with open("Белая гвардия.txt", "r", encoding="utf-8") as inFile:

    reg_expr_list = []

    reg_expr_list.append("\s[Сс]ид[а-я]*[лтвеьмс]?[ьаеойия]?|\s[Сс]иж[а-я]") # ...
    reg_expr_string = '|'.join(reg_expr_list)

    words_set = set()

    for line in inFile.readlines():
        all_results = re.findall(reg_expr_string, line)
        for word in all_results:
    #       print(word[1:])
            words_set.add(word[1:].lower())

    print(*words_set)