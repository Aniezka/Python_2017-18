#Вариант_2
#Задание_3
with open("Ozhegov.txt", "r", encoding='utf-8') as fail:
    tekst = fail.read()
    tekst = tekst.split("\n")
    slova = []
    slovo = "SLOVO"
    while slovo != "":
        slovo = input("Введите слово: ")
        if slovo == "":
            break
        slova.append(slovo)
        for slovo in slova[:-1]:
            flag = False
            for stroka in tekst:
                kusok = stroka.split("|")
                if kusok[0] == slovo:
                    flag = True
                    print(kusok[0], end = "")
                    print("–", end = "")
                    print(kusok[3],end = "")
                    print("–", end = "")
                    print(kusok[1])
            if flag == False:
                print("Не нашел слова ", end = "")
                print(slovo)
    print(slova)
