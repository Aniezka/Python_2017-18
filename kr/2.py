#Вариант_2
#Задание_2
with open("Ozhegov.txt", "r", encoding='utf-8') as fail:
    tekst = fail.readlines()
    kolvo = 0
    for stroka in tekst:
        kusok = stroka.split("|")
        if kusok[2] != "":
            print (stroka)
            kolvo += 1
    print ("Cлов с антонимами: ", kolvo)
