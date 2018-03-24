# эта программа генерирует танку:
# 1 строка - 5 слогов
# 2 строка - 7 слогов
# 3 строка - 5 слогов
# 4 строка - 7 слогов
# 5 строка - 7 слогов


import random

# 1 строка
def noun_sg():
    filename = "noun_sg.txt"
    words_file = open(filename, "r", encoding="utf-8")
    words = words_file.read().split()    
    return random.choice(words)

def noun_pl():
    filename = "noun_pl.txt"
    words_file = open(filename, "r", encoding="utf-8")
    words = words_file.read().split()
    return random.choice(words)

def adj_four_sg():
    filename = "adj_four_sg.txt"
    words_file = open(filename, "r", encoding="utf-8")
    words = words_file.read().split()
    return random.choice(words)

def adj_four_pl():
    filename = "adj_four_pl.txt"
    words_file = open(filename, "r", encoding="utf-8")
    words = words_file.read().split()
    return random.choice(words)

# 2 строка
def verb_two_sg():
    filename = "verb_two_sg.txt"
    words_file = open(filename, "r", encoding="utf-8")
    words = words_file.read().split()
    return random.choice(words)

def verb_two_pl():
    filename = "verb_two_pl.txt"
    words_file = open(filename, "r", encoding="utf-8")
    words = words_file.read().split()
    return random.choice(words)

def noun_acc_pl():
    filename = "noun_acc_pl.txt"
    words_file = open(filename, "r", encoding="utf-8")
    words = words_file.read().split()
    return random.choice(words)

def noun_gen():
    filename = "noun_gen.txt"
    words_file = open(filename, "r", encoding="utf-8")
    words = words_file.read().split()
    return random.choice(words)

def punct():
    return random.choice(['.', '...', '!', '?'])

# 3 строка
def prich_sg():
    filename = "prich_sg.txt"
    words_file = open(filename, "r", encoding="utf-8")
    words = words_file.read().split()
    return random.choice(words)

def noun_nom_sg():
    filename = "noun_nom_sg.txt"
    words_file = open(filename, "r", encoding="utf-8")
    words = words_file.read().split()
    return random.choice(words)

# 4 строка
def verb_1_sg():
    filename = "verb_1_sg.txt"
    words_file = open(filename, "r", encoding="utf-8")
    words = words_file.read().split()
    return random.choice(words)

def pron():
    filename = "pron.txt"
    words_file = open(filename, "r", encoding="utf-8")
    words = words_file.read().split()
    return random.choice(words)

def chast():
    filename = "chast.txt"
    words_file = open(filename, "r", encoding="utf-8")
    words = words_file.read().split()
    return random.choice(words)

# 5 строка
def verb():
    filename = "verb.txt"
    words_file = open(filename, "r", encoding="utf-8")
    words = words_file.read().split()
    return random.choice(words)

def noun():
    filename = "noun.txt"
    words_file = open(filename, "r", encoding="utf-8")
    words = words_file.read().split()
    return random.choice(words)

# сборка строк
def get_line_1(number):
    if number == "sg":
        return ' '.join([noun_sg(), adj_four_sg()])
    return ' '.join([noun_pl(), adj_four_pl()])

def get_line_2(number):
    if number == "sg":
        return ' '.join([verb_two_sg(), noun_acc_pl(), noun_gen()]) + punct()
    return ' '.join([verb_two_pl(), noun_acc_pl(), noun_gen()]) + punct()

def get_line_3():
    return ' '.join([prich_sg(), noun_nom_sg()]) + punct()

def get_line_4():
    return verb_1_sg() + punct() + ' ' + ' '.join([pron(), chast()])

def get_line_5():
    return ' '.join([verb(), noun()]) + punct()

# сборка предложения
def get_tanku():
    number = random.choice(["sg", "pl"])
    print(get_line_1(number))
    print(get_line_2(number))
    print(get_line_3())
    print(get_line_4())
    print(get_line_5())

get_tanku()
