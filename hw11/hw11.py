import re


def read_file():
    file_str = ''
    while file_str == '':
        filename = input('Введите имя файла: ')
        try:
            with open(filename) as html_file:
                file_str = html_file.read() # считываем файл в строку
                return file_str # и возвращаем ее
        except:
            print('Ошибка') # если не удалось открыть файл, выводим сообщение об ошибке

def replace_words(file_str):
    new_text = file_str
    new_text = re.sub(r'Птиц(а\W)', r'Рыб\1', new_text)
    new_text = re.sub(r'птиц(а\W)', r'рыб\1', new_text)
    new_text = re.sub(r'Птиц(ы\W)', r'Рыб\1', new_text)
    new_text = re.sub(r'птиц(ы\W)', r'рыб\1', new_text)
    new_text = re.sub(r'Птиц(е\W)', r'Рыб\1', new_text)
    new_text = re.sub(r'птиц(е\W)', r'рыб\1', new_text)
    new_text = re.sub(r'Птиц(у\W)', r'Рыб\1', new_text)
    new_text = re.sub(r'птиц(у\W)', r'рыб\1', new_text)
    new_text = re.sub(r'Птицей(\W)', r'Рыбой\1', new_text)
    new_text = re.sub(r'птицей(\W)', r'рыбой\1', new_text)
    new_text = re.sub(r'Птиц(\W)', r'Рыб\1', new_text)
    new_text = re.sub(r'птиц(\W)', r'рыб\1', new_text)
    new_text = re.sub(r'Птиц(ам\W)', r'Рыб\1', new_text)
    new_text = re.sub(r'птиц(ам\W)', r'рыб\1', new_text)
    new_text = re.sub(r'Птиц(ами\W)', r'Рыб\1', new_text)
    new_text = re.sub(r'птиц(ами\W)', r'рыб\1', new_text)
    new_text = re.sub(r'Птиц(ах\W)', r'Рыб\1', new_text)
    new_text = re.sub(r'птиц(ах\W)', r'рыб\1', new_text)
    new_text = re.sub(r'Пти́ц(ы\W)', r'Рыб\1', new_text)
    return new_text
        
def write_to_file(new_text):
    with open('Птицы->рыбы.txt', 'w', encoding='utf-8') as result_file: # безопасное открытие файла
        result_file.write(new_text)

article_birds = read_file()
article_fishes = replace_words(article_birds)
write_to_file(article_fishes)
