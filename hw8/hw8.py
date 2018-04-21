# Вариант_7
import random
 

def make_dict(filename):
    s = {}
    with open(filename, encoding='utf-8') as f:
        for line in f: # проходим по строчкам файла
            k = line.split() # k - массив из слов строки: НАПРИМЕР [маркер, перманентный, текстовыделяющий]
            s[k[0]] = k[1:] # добавляем в словарь пару: маркер, [перманентный, текстовыделяющий] (строка, список)
    return s
 
 
def print_res(vars):
    print(random.choice(vars))
 
 
def main():
    s = make_dict("slovar.txt")
    winer = ['Молодец', 'Вы выиграли', 'Успех', 'Точно так']
    loser = ['Увы', 'А вот и нет', 'Вы проиграли']
    word = list(s.keys())[random.randint(0, len(s) - 1)] # случайное из слов, которые мы хотим отгадать
    clue = random.choice(s[word]) # случайная подсказка к угадываемому слову
    print(clue, '...')
    for j in range(6): # игроку дается 6 попыток
        print('Введите слово:')
        answer = input() # считываем попытку
        if answer == word: # если попытка - успешная
            print_res(winer) # пеачтаем одну из форм "поздравления"
            break
    if answer != word: # если ни одна из попыток не увенчалась успехом
        print_res(loser) # печатаем одну из форм "соболезнования"

 
 
 
 
main()
