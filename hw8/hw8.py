# Вариант_7
import random
 
 
def make_dict(filename):
    s = {}
    with open(filename, encoding='utf-8') as f:
        for line in f:
            k = line.split()
        s[k[0]] = k[1:]
    return s
 
 
def print_res(vars):
    print(random.choice(vars))
 
 
def main():
    s = make_dict("slovar.txt")
    winer = ['Молодец', 'Вы выиграли', 'Успех', 'Точно так']
    loser = ['Увы', 'А вот и нет', 'Вы проиграли']
    word = list(s.keys())[random.randint(0, len(s) - 1)]
    clue = random.choice(s[word])
    print(clue, '...')
    for j in range(6):
        print('Введите слово:')
        answer = input()
        if answer == word:
            print_res(winer)
            break
    if answer != word:
        print_res(loser)
 
 
 
 
main()
